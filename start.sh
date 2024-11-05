#!/bin/bash

# 기존에 실행 중인 uvicorn 프로세스를 찾고 종료
PID=$(lsof -t -i:5011)
if [ -n "$PID" ]; then
    echo "Stopping existing server on port 5011..."
    kill -9 $PID
fi

# 최신 코드 가져오기
echo "Pulling latest changes from Git repository..."
git pull origin master

# 백그라운드에서 uvicorn 서버 시작
echo "Starting server..."
nohup poetry run uvicorn app.main:app --reload --host 220.69.209.126 --port 5011 &

echo "Server started successfully!"
