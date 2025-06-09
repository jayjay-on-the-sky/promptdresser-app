#!/bin/bash

# Load Conda into current shell (important for macOS)
source $(conda info --base)/etc/profile.d/conda.sh

# Activate your virtual environment
conda activate promptdresser

# Navigate to your project directory (optional, edit if needed)
cd "$(dirname "$0")"

# Run the try-on inference script
python run_tryon.py
