#!/usr/bin/env bash

set -e

VENV=".venv"

if [ ! -d "$VENV" ]; then
  python3 -m venv "$VENV"
fi

source "$VENV/bin/activate"

exec "$SHELL"
