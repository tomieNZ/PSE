#!/bin/bash
# One-click Docker build & run script for CV ATS Agent

IMAGE_NAME="cv-ats-agent"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Check .env exists
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "❌ .env not found. Run: cp .env.example .env and fill in your API key."
    exit 1
fi

# Check docs directory
if [ ! -d "$SCRIPT_DIR/docs" ]; then
    echo "❌ docs/ directory not found. Please add your CV PDF and JD text file."
    exit 1
fi

# Build & Run
echo "🔨 Building Docker image..."
docker build -t "$IMAGE_NAME" "$SCRIPT_DIR" && \
echo "🚀 Running analysis..." && \
docker run --rm --env-file "$SCRIPT_DIR/.env" -v "$SCRIPT_DIR/docs:/app/docs" "$IMAGE_NAME"
