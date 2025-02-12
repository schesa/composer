#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the composer directory
cd "$SCRIPT_DIR"

# Show current directory and files for debugging
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la

# Build the Docker image with verbose output and load it into Docker
echo "Building Docker image..."
docker buildx build -t chatbot . --progress=plain --load

# Run the container with interactive mode and pseudo-TTY
echo "Starting chatbot..."
docker run -it --rm chatbot 