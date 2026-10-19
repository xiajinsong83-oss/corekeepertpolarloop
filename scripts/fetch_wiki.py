#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core Keeper Hub - atma.gg Wiki 变动聚合脚本（P1-1）
=============================================================
数据源 : corekeeper.atma.gg（MediaWiki API，/english/api.php）
频率   : 与 Steam 新闻管道同一 GitHub Actions cron（每 6 小时）
产出   :
  1. data/wiki_updates.json   （最近 25 条主命名空间改动，供聚合页 + 首页区块）

守卫规则（对齐调研报告 Lagos Life 案例）:
  - 解析失败 / 条数异常（<3）→ 退出码 1，不写脏数据（保留旧文件）
  - 写临时文件再原子替换，避免半写入
  - UA 标注站点域名，礼貌抓取（30s 超时）
"""

import json
import os
import random
import sys
import time
import urllib.request

API_URL = (
    "https://corekeeper.atma.gg/english/api.php"
    "?action=query&list=recentchanges&rcnamespace=0&rclimit=25"
    "&rcprop=title|timestamp|user|comment|ids&format=json"
)
BASE_URL = "https://corekeeper.atma.gg/en/"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON = os.path.join(BASE_DIR, "data", "wiki_updates.json")

UA = "Mozilla/5.0 (compatible; CoreKeeperHub/1.0; +https://www.polarloop.cn)"
MIN_ITEMS = 3
MAX_ATTEMPTS = 3
RETRY_WAIT = 20  # 秒；atma.gg 对密集请求会临时限流，退避重试


def fetch_json(url, attempts=MAX_ATTEMPTS):
    last_err = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            last_err = e
            if i < attempts - 1:
                print(f"  retry {i+1}/{attempts} after error: {e}")
                time.sleep(RETRY_WAIT)
    raise last_err


def normalize(rows):
    out = []
    seen = set()
    for r in rows:
        if r.get("ns", 0) != 0:
            continue
        title = r.get("title", "").strip()
        if not title or title in seen:
            continue
        seen.add(title)
        ts = r.get("timestamp", "")
        out.append({
            "title": title,
            "url": BASE_URL + title.replace(" ", "_"),
            "ts": ts,
            "user": r.get("user", ""),
            "comment": r.get("comment", "").strip(),
            "type": r.get("type", "edit"),
        })
    return out


def main():
    print("==> Fetching atma.gg recent changes...")
    try:
        data = fetch_json(API_URL)
        rows = data.get("query", {}).get("recentchanges", [])
    except Exception as e:
        print(f"!! Fetch failed: {e}")
        return 1

    updates = normalize(rows)
    if len(updates) < MIN_ITEMS:
        print(f"!! Guard: only {len(updates)} items (< {MIN_ITEMS}), keeping old file")
        return 1

    # 每次随机选取 3 条栏目内容（用户要求）
    updates = random.sample(updates, min(3, len(updates)))
    print(f"==> Randomly picked {len(updates)} wiki updates for this round")

    payload = {
        "checkedAt": __import__("time").strftime("%Y-%m-%dT%H:%M:%SZ", __import__("time").gmtime()),
        "updates": updates,
    }
    tmp = DATA_JSON + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA_JSON)
    print(f"==> Wiki updates: {len(updates)} items written to data/wiki_updates.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
