#!/bin/bash

# Define the path to the Gunicorn PID file
PID_FILE="/run/gunicorn.pid"

# Check if the PID file exists
if [ -f "$PID_FILE" ]; then
    # Send a HUP signal to the Gunicorn master process to gracefully reload workers
    echo "Reloading Gunicorn gracefully..."
    kill -HUP "$(cat $PID_FILE)"
    echo "Gunicorn reloaded successfully."
else
    echo "Error: Gunicorn PID file not found. Gunicorn may not be running."
fi
