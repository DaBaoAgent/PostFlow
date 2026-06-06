#!/bin/bash
# social-auto-upload wrapper — 从任何目录调用 sau CLI
# 用法: sau <platform> <action> [args...]
SAU_DIR="D:/@kaifa/social-auto-upload"
cd "$SAU_DIR" && .venv/Scripts/python -m sau_cli "$@"
