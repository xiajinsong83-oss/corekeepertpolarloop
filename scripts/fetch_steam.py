#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core Keeper Hub - Steam 官方新闻抓取脚本（P0-2 Patch Notes 自动追踪）
=============================================================
数据源 : Steam 官方新闻 RSS / JSON API（AppID 1621690）
频率   : GitHub Actions cron 每 6 小时一次（分钟位错开整点）
产出   :
  1. content/news/YYYY-MM-DD-<gid>.md   （每条新条目一个页面）
  2. data/steam_news.json               （全部条目，供首页「最新更新」区块）

守卫规则（来自调研报告 Lagos Life 案例）:
  - 条数异常（<3）直接退出码 1，不写脏数据
  - append 不覆盖：已有 guid 跳过，只写新条目
  - RSS description 是转义 HTML，反转义清洗后再写入，不原样塞 Markdown
  - checkedAt / changedAt 双时间戳：checkedAt=本次核对时间，changedAt=数据真实变化时间
"""

import html
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

APP_ID = "1621690"
RSS_URL = f"https://store.steampowered.com/feeds/news/app/{APP_ID}/?l=english"
JSON_API_URL = (
    f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
    f"?appid={APP_ID}&count=30&maxlength=0&format=json"
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_DIR = os.path.join(BASE_DIR, "content", "news")
DATA_JSON = os.path.join(BASE_DIR, "data", "steam_news.json")

UA = "Mozilla/5.0 (compatible; CoreKeeperHub/1.0; +https://www.polarloop.cn)"
MIN_ITEMS = 3  # 条数守卫：少于该值视为抓取异常

# 标题匹配补丁的正则（patch notes / hotfix / version）
PATCH_RE = re.compile(r"(patch|hotfix|version|update|1\.\d)", re.I)


def fetch(url: str) -> str:
    """拉取远程内容，超时 30s，失败抛异常。"""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_rss(xml_text: str):
    """解析 RSS 2.0，返回条目列表 [{guid,title,link,pubDate,description}]。"""
    items = []
    root = ET.fromstring(xml_text)
    for item in root.iter("item"):
        guid = (item.findtext("guid") or item.findtext("link") or "").strip()
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        desc = (item.findtext("description") or "").strip()
        if not guid or not title:
            continue
        items.append(
            {
                "guid": guid,
                "title": title,
                "link": link,
                "pubDate": pub_date,
                "description": html.unescape(desc),
            }
        )
    return items


def parse_json(json_text: str):
    """解析 Steam JSON API 作为后备源。

    注意：JSON API 的 gid 与 RSS 的 guid（URL）不互通，同篇新闻两个源
    标识不同。因此仅保留官方 feedlabel "Community Announcements"（Patch
    Notes 与官方公告所在频道），剔除第三方组（如 PlayGround.ru 等）；
    去重指纹用 (title, pubDate) 组合，避免与 RSS 条目重复写入。
    """
    items = []
    data = json.loads(json_text)
    for news in data.get("appnews", {}).get("newsitems", []):
        feedlabel = (news.get("feedlabel") or "").strip()
        # 只保留官方公告频道，跳过第三方内容组
        if feedlabel != "Community Announcements":
            continue
        items.append(
            {
                "guid": f"json-{news.get('gid', '')}",
                "title": news.get("title", "").strip(),
                "link": news.get("url", "").strip(),
                "pubDate": time.strftime(
                    "%a, %d %b %Y %H:%M:%S +0000",
                    time.gmtime(news.get("date", 0)),
                ),
                "description": html.unescape(news.get("contents", "") or ""),
            }
        )
    return items


def clean_text(raw: str, max_len: int = 240) -> str:
    """清洗 RSS 转义 HTML：去标签、折叠空白、截断为摘要。"""
    text = re.sub(r"<[^>]+>", "", raw)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip() + "…"
    return text


def slugify(title: str) -> str:
    """标题转小写连字符文件名（去特殊字符）。"""
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:70].strip("-") or "news"


def guess_type(title: str) -> str:
    """按标题打类型标签：patch / event / blog。"""
    if PATCH_RE.search(title):
        return "patch"
    return "event"


def norm_title(t: str) -> str:
    """归一化标题做指纹：折叠空白、统一连字符，消除 RSS/JSON 双源细微差异。"""
    return re.sub(r"\s+", " ", t).strip().lower()


def norm_date(d: str) -> str:
    """归一化日期做指纹：只保留 YYYY-MM-DD。"""
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", d)
    if m:
        return m.group(0)
    return d[:10]


def main():
    print("==> Fetching Steam news...")
    try:
        rss_text = fetch(RSS_URL)
        items = parse_rss(rss_text)
    except Exception as exc:  # RSS 失败则尝试 JSON API
        print(f"RSS failed ({exc}), falling back to JSON API...")
        try:
            json_text = fetch(JSON_API_URL)
            items = parse_json(json_text)
        except Exception as exc2:
            print(f"JSON API also failed: {exc2}", file=sys.stderr)
            sys.exit(1)

    if len(items) < MIN_ITEMS:
        print(
            f"GUARD: only {len(items)} items (< {MIN_ITEMS}), refusing to write dirty data",
            file=sys.stderr,
        )
        sys.exit(1)

    # 读取既有 json（若有），跳过已收录条目
    # 去重指纹：guid（RSS URL / json-gid）+ 兜底 (norm_title, norm_date) 防止跨源重复
    existing = {}
    if os.path.exists(DATA_JSON):
        try:
            with open(DATA_JSON, "r", encoding="utf-8") as f:
                existing = {it["guid"]: it for it in json.load(f).get("items", [])}
        except Exception:
            existing = {}

    existing_fp = {
        (norm_title(it.get("title", "")), norm_date(it.get("pubDate", "")))
        for it in existing.values()
    }

    changed_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    new_items = []
    written_files = 0

    os.makedirs(NEWS_DIR, exist_ok=True)

    for item in items:
        guid = item["guid"]
        if guid in existing:
            continue
        # 跨源指纹去重：归一化标题+日期相同视为同一篇（RSS/JSON 双源场景）
        fp = (norm_title(item["title"]), norm_date(item["pubDate"]))
        if fp in existing_fp:
            continue
        existing_fp.add(fp)  # 本批次内也去重（RSS 可能包含重复语言版本）
        typ = guess_type(item["title"])
        pub = item["pubDate"]
        # pubDate → YYYY-MM-DD（容错解析）
        try:
            pub_ts = time.mktime(time.strptime(pub, "%a, %d %b %Y %H:%M:%S %z"))
            day = time.strftime("%Y-%m-%d", time.localtime(pub_ts))
        except Exception:
            day = time.strftime("%Y-%m-%d")

        summary = clean_text(item["description"])
        fname = f"{day}-{slugify(item['title'])}-{guid[-8:]}"
        # 防止文件名冲突：若已存在同 slug 文件且 guid 不同，加序号
        n = 2
        fpath = os.path.join(NEWS_DIR, fname + ".md")
        while os.path.exists(fpath):
            fpath = os.path.join(NEWS_DIR, f"{fname}-{n}.md")
            n += 1

        fm = f"""---
title: "{item['title']}"
date: "{pub}"
type: "{typ}"
feedlabel: "Steam News"
link: "{item['link']}"
description: "{summary}"
---

{summary}

> Auto-tracked from the official Steam announcement feed (AppID {APP_ID}). This page is a summary — [read the original announcement]({item['link']}).
"""
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(fm)
        written_files += 1

        new_items.append(
            {
                "guid": guid,
                "title": item["title"],
                "link": item["link"],
                "pubDate": pub,
                "type": typ,
                "summary": summary,
                "page": f"/news/{os.path.basename(fpath)[:-3]}/",
                "changedAt": changed_at,
            }
        )

    # 合并写回 json（append 不覆盖；checkedAt 全量刷新）
    merged_items = list(existing.values())
    merged_items.extend(new_items)
    merged = {
        "source": "https://store.steampowered.com/feeds/news/app/1621690/?l=english",
        "appid": APP_ID,
        "checkedAt": changed_at,
        "items": merged_items,
    }
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"==> New items: {len(new_items)}, files written: {written_files}")
    if written_files == 0:
        print("No changes - skip commit")
        sys.exit(0)
    print("Changes detected - commit & push")
    sys.exit(0)


if __name__ == "__main__":
    main()
