#!/usr/bin/env bash
set -euo pipefail
: "${V75_URL:?Set V75_URL to your published app address}"
: "${V75_API_KEY:?Set V75_API_KEY to your generated worker key}"
ollama pull "${OLLAMA_MODEL:-qwen2.5vl:7b}"
exec python3 "$(dirname "$0")/v75_worker.py"
