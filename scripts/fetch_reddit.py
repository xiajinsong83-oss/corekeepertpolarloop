#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core Keeper Hub - Reddit 社区热议聚合脚本（P2-1，方案 C）
=============================================================
数据源 : r/CoreKeeper（Reddit JSON API 主源，.rss 后备）
频率   : 与 Steam 新闻 / Wiki 聚合同一 GitHub Actions cron（每 6 小时）
产出   :
  1. data/reddit_hot.json   （热门帖 top N：标题/作者/分数/链接/时间，供首页卡片墙）

守卫规则（与 fetch_wiki.py 对齐）:
  - 解析失败 / 条数异常（<3）→ 退出码 1，不写脏数据（保留旧文件）
  - 写临时文件再原子替换
  - 自定义 UA 礼貌抓取；Reddit 对无 UA 请求返回 429
注意   : 本地开发网络可能无法访问 reddit.com（HTTP:000），但 GitHub
         Actions runner（美国机房）通常可达；管道在 CI 首次运行后自动填充数据。
"""

import json
import os
import sys
import time
import urllib.request

REDDIT_JSON = "https://www.reddit.com/r/CoreKeeper/hot.json?limit=12&raw_json=1"
REDDIT_RSS = "https://www.reddit.com/r/CoreKeeper/.rss"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON = os.path.join(BASE_DIR, "data", "reddit_hot.json")

UA = "Mozilla/5.0 (compatible; CoreKeeperHub/1.0; +https://www.polarloop.cn)"
MIN_ITEMS = 3
MAX_ATTEMPTS = 3
RETRY_WAIT = 20


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/json, text/xml, */*",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_retry(url, attempts=MAX_ATTEMPTS):
    last = None
    for i in range(attempts):
        try:
            return fetch(url)
        except Exception as e:
            last = e
            if i < attempts - 1:
                print(f"  retry {i+1}/{attempts} after error: {e}")
                time.sleep(RETRY_WAIT)
    raise last


def normalize(posts):
    out, seen = [], set()
    for p in posts:
        title = (p.get("data", {}).get("title") or "").strip() if isinstance(p, dict) else ""
        if not title or title in seen:
            continue
        seen.add(title)
        d = p["data"] if isinstance(p, dict) else {}
        permalink = d.get("permalink", "")
        out.append({
            "title": title,
            "author": d.get("author", ""),
            "score": d.get("ups", 0),
            "url": "https://www.reddit.com" + permalink if permalink.startswith("/") else d.get("url", ""),
            "ts": d.get("created_utc", ""),
        })
    return out


def parse_json_api(text):
    data = json.loads(text)
    return normalize(data.get("data", {}).get("children", []))


def _strip_cdata(s):
    """剥离 <![CDATA[...]]> 包裹（标准 RSS 常见）"""
    if s.startswith("<![CDATA[") and s.endswith("]]>"):
        return s[9:-3]
    return s


def parse_rss(text):
    """后备：Reddit .rss（仅 title/link/author，无 score 时 score 记 0 并在首页隐藏分数）"""
    import re
    items = re.findall(r"<item>(.*?)</item>", text, re.S)
    posts = []
    for it in items:
        def grab(tag):
            m = re.search(r"<%s[^>]*>(.*?)</%s>" % (tag, tag), it, re.S)
            return _strip_cdata(m.group(1).strip()) if m else ""
        title = grab("title")
        if not title:
            continue
        link = grab("link")
        author = _strip_cdata(grab("dc:creator"))
        posts.append({"title": title, "author": author, "score": 0,
                      "url": link, "ts": ""})
    return posts


def main():
    print("==> Fetching r/CoreKeeper hot posts...")
    try:
        text = fetch_retry(REDDIT_JSON)
        posts = parse_json_api(text)
    except Exception as e:
        print(f"!! JSON API failed ({e}), trying RSS fallback...")
        try:
            text = fetch_retry(REDDIT_RSS)
            posts = parse_rss(text)
        except Exception as e2:
            print(f"!! RSS fallback failed too: {e2}")
            return 1

    if len(posts) < MIN_ITEMS:
        print(f"!! Guard: only {len(posts)} items (< {MIN_ITEMS}), keeping old file")
        return 1

    payload = {
        "checkedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "posts": posts[:12],
    }
    tmp = DATA_JSON + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA_JSON)
    print(f"==> Reddit hot: {len(payload['posts'])} posts written to data/reddit_hot.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
