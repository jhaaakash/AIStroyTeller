#!/bin/bash

# Setup script for the AI Storytelling Application

echo "Setting up AI Storytelling Application..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file has been configured
if grep -q "your_openai_api_key_here" .env; then
    echo ""
    echo "⚠️  WARNING: You need to set your OpenAI API key in the .env file before running the application."
    echo "Please edit the .env file and replace 'your_openai_api_key_here' with your actual API key."
    echo ""
fi

echo "Setup complete! You can now run the application with:"
echo "python run.py"