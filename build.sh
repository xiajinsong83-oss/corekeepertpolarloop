#!/bin/bash
# Core Keeper Hub - Hugo 构建脚本（Cloudflare Pages 使用）
# 说明：若 static 会被清空再整体复制，长期保留图片请放 data-src/package/images/ 随构建拷贝
set -e

echo "==> Hugo build starting"

# 拷贝长期保留的像素图标库（data-src -> static），防 build.sh 清空 static
if [ -d "data-src/package/images" ] && [ -n "$(ls -A data-src/package/images 2>/dev/null)" ]; then
  mkdir -p static/img
  cp -rn data-src/package/images/* static/img/ 2>/dev/null || true
fi

# 构建到 public/
hugo --minify

echo "==> Hugo build finished"
