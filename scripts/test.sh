#!/usr/bin/env bash
set -euo pipefail

python3 scripts/check_docs.py
python3 scripts/check_automation.py
