#!/bin/bash

PORT=8080
DIR="$(cd "$(dirname "$0")" && pwd)"

# 해당 포트 사용 중인 프로세스 종료
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
  echo "포트 $PORT 사용 중인 프로세스 (PID: $PID) 종료 중..."
  kill -9 $PID
  sleep 0.5
fi

echo "서버 시작: http://localhost:$PORT"
echo "종료: Ctrl+C"

# Python 버전에 따라 서버 실행
if command -v python3 &>/dev/null; then
  cd "$DIR" && python3 -m http.server $PORT
elif command -v python &>/dev/null; then
  cd "$DIR" && python -m SimpleHTTPServer $PORT
else
  echo "Python이 설치되어 있지 않습니다."
  exit 1
fi
