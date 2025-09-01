#!/bin/bash

echo "BUILD START"

# Install pip if not available
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py
fi

# Upgrade pip
python3.9 -m pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=core.settings

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
