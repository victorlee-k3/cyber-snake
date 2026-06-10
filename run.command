#!/bin/bash
# Change to the directory where this script is located
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

# Run the game
python main.py
