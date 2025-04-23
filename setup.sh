#!/bin/bash

# Activate virtual environment based on OS
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # macOS or Linux
    echo "Activating virtual environment on macOS/Linux..."
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    echo "Activating virtual environment on Windows..."
    source venv/Scripts/activate
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete! Your virtual environment is now active and dependencies are installed."
echo "Don't forget to add your actual API keys to the .env file." 