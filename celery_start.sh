#!/bin/bash

source .venv/bin/activate

echo "Starting Celery Beat..."
celery -A celery_app beat &
BEAT_PID=$!

echo "Starting Celery Worker..."
celery -A celery_app worker -c 4 &
WORKER_PID=$!

echo "Celery Beat (PID: $BEAT_PID) and Worker (PID: $WORKER_PID) are running."