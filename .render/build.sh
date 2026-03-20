#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Create necessary directories
mkdir -p logs
mkdir -p uploads
