#!/bin/bash
set -e

echo
cat << "EOF"
      __   __   ___   _      ___
      \ \ / /  / _ \ | |    / _ \
       \ V /  | | | || |   | | | |
        | |   | |_| || |___| |_| |
        |_|    \___/ |_____|\___/

      YOLO Flask Object Detection API
EOF
echo

echo "[FIX]: Fixing volume permissions"

mkdir -p /app/uploads /app/outputs /app/data
chmod -R 777 /app/uploads /app/outputs /app/data

echo
echo "Current permissions"
ls -la /app/uploads
ls -la /app/outputs
ls -la /app/data

echo
echo "[HOLD THE DOOR]: Starting Flask application"
echo

exec python app.py
