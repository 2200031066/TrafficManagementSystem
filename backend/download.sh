#!/usr/bin/env bash

set -euo pipefail

cat << "EOF"
      __   __   ___   _      ___
      \ \ / /  / _ \ | |    / _ \
       \ V /  | | | || |   | | | |
        | |   | |_| || |___| |_| |
        |_|    \___/ |_____|\___/

      YOLOv4 Weights and Config Downloader
EOF

URL="https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre"
FILES=(
  "yolov4.cfg"
  "yolov4.weights"
  "yolov4-tiny.cfg"
  "yolov4-tiny.weights"
)

download() {
  local file="$1"
  if [[ -f "$file" ]]; then
    echo "[skip] $file already exists"
    return
  fi
  echo "[download] $file"
  curl -L -o "$file" "$URL/$file"
}

main() {
  for f in "${FILES[@]}"; do
    download "$f"
  done
  echo "YOLO files ready in $(pwd)"
}

main "$@"
