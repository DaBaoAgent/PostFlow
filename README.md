<!-- README-PROMO:START -->
<p align="center">
  <img src="assets/readme/hero.webp" alt="PostFlow：一条命令将视频和图文自动分发到多个社交媒体平台" width="100%" />
  <img src="assets/readme/workflow.webp" alt="PostFlow 工作流：准备内容、账号登录、拟人发布与多平台分发" width="100%" />
  <img src="assets/readme/beginner.webp" alt="PostFlow 新手上手：登录一次，通过命令行定时发布到七个平台" width="100%" />
</p>
<!-- README-PROMO:END -->

# 🚀 PostFlow — 一键分发，流量自来

<h4 align="center">Multi-Platform Social Media Auto Publisher | 多平台社交媒体自动发布工具</h4>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/platforms-7-orange" alt="Platforms">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs">
</p>

<p align="center">
  <b>English</b> | <a href="#中文">中文</a>
</p>

---

## English

### What is PostFlow?

PostFlow is an open-source **multi-platform social media auto-publishing tool** that lets you publish videos and image-text posts to **7 platforms** with a single command. Built on **Patchright** (anti-detection browser automation), it simulates real human operations — staggered typing, random pauses, natural scrolling — to minimize platform detection.

> **Forked and enhanced from [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload) (9K+ stars)**. PostFlow adds human-like delay strategies, location tagging, improved CLI, bilingual documentation, and production-hardened reliability.

### Supported Platforms

| Platform | Video | Image+Text | Schedule | Location | Original Declaration | CLI |
|----------|:-----:|:----------:|:--------:|:--------:|:--------------------:|:---:|
| **Douyin** (抖音) | ✅ | ✅ | ✅ | ✅ | ✅ | `postflow douyin` |
| **Xiaohongshu** (小红书) | ✅ | ✅ | ✅ | ✅ | ✅ | `postflow xiaohongshu` |
| **Kuaishou** (快手) | ✅ | ✅ | ✅ | ❌ | ❌ | `postflow kuaishou` |
| **Bilibili** (B站) | ✅ | ❌ | ✅ | ❌ | ❌ | `postflow bilibili` |
| **WeChat Channels** (视频号) | ✅ | ❌ | ✅ | ❌ | ✅ | `postflow tencent` |
| **TikTok** | ✅ | ❌ | ✅ | ❌ | ❌ | examples |
| **Baijiahao** (百家号) | ✅ | ❌ | ✅ | ❌ | ❌ | examples |

### Quick Start

```bash
# Clone
git clone https://github.com/DaBaoAgent/PostFlow.git
cd PostFlow

# Install (requires Python 3.10+)
uv venv
uv pip install -e .

# Install browser driver
patchright install chromium

# Copy config
cp conf.example.py conf.py

# Login & Publish
postflow xiaohongshu login --account myaccount --headed
postflow xiaohongshu upload-note --account myaccount \
  --images img1.png img2.png --title "My First Post" \
  --note "Hello World!" --tags tag1,tag2 \
  --location "Shanghai" --headed
```

### Key Features

- 🧠 **Human-like Behavior** — randomized typing speed (30-150ms/char), natural pauses (0.5-3s), scroll-before-click, mimics real user rhythm
- 🔐 **Cookie Persistence** — login once, reuse forever (Playwright storage_state)
- 📅 **Scheduled Publishing** — set exact publish time per platform
- 📍 **Location Tagging** — add POI/location to Douyin & Xiaohongshu posts
- 🏷️ **Auto Tagging** — automatic hashtag insertion with dropdown selection
- ✅ **Original Declaration** — auto-check original content checkbox
- 🖥️ **Headless Mode** — run in background without visible browser
- 🔧 **Modular** — each platform is an independent uploader, easy to extend

### Tech Stack

- **Python 3.10+** with asyncio
- **Patchright 1.58** (Playwright fork with enhanced anti-detection)
- **Chromium** for browser automation
- **uv** for package management

### Why PostFlow over social-auto-upload?

| Feature | social-auto-upload | PostFlow |
|---------|:---:|:---:|
| Human-like delays | ❌ | ✅ Random pauses + char-by-char typing |
| Location tagging (Douyin) | ❌ | ✅ |
| Location tagging (XHS) | ❌ | ✅ Fixed selector for new UI |
| Bilingual docs | ❌ | ✅ CN/EN |
| Cookie privacy | Exposed in repo | ✅ .gitignored |
| Production tested | Community | ✅ 50+ real posts |

### Contributors

- **Dabao** (DaBaoAgent) — lead developer, human-like strategy, location features, bilingual docs
- Original project by [dreammis](https://github.com/dreammis) and [contributors](https://github.com/dreammis/social-auto-upload/graphs/contributors)

---

<h2 id="中文">中文</h2>

### PostFlow 是什么？

PostFlow 是一个开源的**多平台社交媒体自动发布工具**，一条命令即可将视频和图文内容发布到 **7 个主流平台**。基于 **Patchright**（增强反检测的浏览器自动化框架），模拟真人的打字节奏、随机停顿、自然滚动等行为，大幅降低被平台检测的风险。

> **基于 [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload)（9K+ Star）进行迭代优化**。PostFlow 新增真人化延迟策略、位置标记、CLI 增强、中英双语文档，生产环境验证通过。

### 支持平台

| 平台 | 视频 | 图文 | 定时 | 位置 | 原创声明 | CLI |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| 抖音 | ✅ | ✅ | ✅ | ✅ | ✅ | `postflow douyin` |
| 小红书 | ✅ | ✅ | ✅ | ✅ | ✅ | `postflow xiaohongshu` |
| 快手 | ✅ | ✅ | ✅ | ❌ | ❌ | `postflow kuaishou` |
| B站 | ✅ | ❌ | ✅ | ❌ | ❌ | `postflow bilibili` |
| 视频号 | ✅ | ❌ | ✅ | ❌ | ✅ | `postflow tencent` |
| TikTok | ✅ | ❌ | ✅ | ❌ | ❌ | examples |
| 百家号 | ✅ | ❌ | ✅ | ❌ | ❌ | examples |

### 快速开始

```bash
git clone https://github.com/DaBaoAgent/PostFlow.git
cd PostFlow
uv venv && uv pip install -e .
patchright install chromium
cp conf.example.py conf.py

# 扫码登录（有头模式弹出浏览器窗口）
postflow xiaohongshu login --account 我的账号 --headed

# 发布图文
postflow xiaohongshu upload-note --account 我的账号 \
  --images 图1.png 图2.png --title "我的标题" \
  --note "正文内容" --tags 标签1,标签2 \
  --location "上海" --headed
```

### 核心亮点

- 🧠 **真人操作模拟** — 逐字输入（30-150ms随机延迟）、随机停顿（0.5-3s）、先滚动再点击，彻底告别机器人痕迹
- 🔐 **一次登录永久复用** — 基于Playwright storage_state，Cookie持久化无需反复扫码
- 📅 **定时发布** — 精确到分钟的定时发布，支持提前排期
- 📍 **位置标记** — 抖音、小红书支持添加POI地理位置
- 🏷️ **自动标签** — 话题标签自动输入并从下拉列表点选
- ✅ **原创声明** — 自动勾选原创内容复选框
- 🖥️ **无头模式** — 后台静默运行，不弹浏览器窗口
- 🔧 **模块化架构** — 每个平台独立uploader，易扩展

### 适用场景

- 🏪 **本地商家** — 轮椅租赁、餐饮、家政等，用美女/产品图文引流到店
- 🎬 **自媒体创作者** — 一键分发到抖音+B站+小红书，节省80%重复操作时间
- 🛒 **电商运营** — 商品种草内容多平台同步发布
- 🤖 **AI Agent 工作流** — 作为Hermes/OpenClaw/Codex等AI Agent的发布终端

### 技术栈

- **Python 3.10+** + asyncio 异步架构
- **Patchright 1.58** — Playwright 增强反检测分支
- **Chromium** 浏览器自动化引擎
- **uv** 包管理器

### 与 social-auto-upload 的差异

| 特性 | social-auto-upload | PostFlow |
|------|:---:|:---:|
| 真人化延迟 | ❌ | ✅ 随机停顿+逐字输入 |
| 抖音位置标记 | ❌ | ✅ CLI --location |
| 小红书位置标记 | 选择器旧 | ✅ 适配最新UI |
| 中英文档 | ❌ | ✅ 完整双语 |
| Cookie隐私 | 可能泄露 | ✅ .gitignore保护 |
| 生产测试 | 社区 | ✅ 50+ 真实发布 |

### 贡献者

- **大宝 Dabao** (DaBaoAgent) — 主力开发，真人化策略、位置功能、双语文档
- 原项目作者 [dreammis](https://github.com/dreammis) 及所有 [贡献者](https://github.com/dreammis/social-auto-upload/graphs/contributors)

### Star History

如果这个项目对你有帮助，请给一个 ⭐ Star！

---

<p align="center">
  <sub>Built with ❤️ by <a href="https://github.com/DaBaoAgent">Dabao</a> | Forked from <a href="https://github.com/dreammis/social-auto-upload">social-auto-upload</a></sub>
</p>
