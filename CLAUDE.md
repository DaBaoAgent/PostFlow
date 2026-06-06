## Project Overview

`PostFlow` is a powerful automation tool designed to help content creators and operators efficiently publish video and image-text content to multiple social media platforms. Forked and enhanced from `social-auto-upload` (9K+ stars).

### Supported Platforms
Douyin (抖音), Xiaohongshu (小红书), Kuaishou (快手), Bilibili (B站), WeChat Channels (视频号), TikTok, Baijiahao (百家号)

### Key Enhancements over social-auto-upload
- Human-like behavior simulation (random delays, char-by-char typing)
- Location/POI tagging for Douyin & Xiaohongshu
- Bilingual documentation (CN/EN)
- Cookie privacy protection
- Production-verified (50+ real posts)

### CLI Entry Point
```bash
postflow <platform> <action> [args]
```
Formerly `sau`, now unified under `postflow`.

### Installation
```bash
uv venv && uv pip install -e .
patchright install chromium
cp conf.example.py conf.py
```

### Development
- Python 3.10+ with asyncio
- Patchright 1.58 for browser automation
- Each platform in `uploader/<platform>_uploader/main.py`
- CLI entry: `sau_cli.py`
- Cookies excluded via .gitignore
