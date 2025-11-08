# Use official Python runtime as base image
# 'slim' version is smaller (saves space) but has everything we need
FROM python:3.11-slim

# Set working directory inside container
# All commands will run from here
WORKDIR /app

# Copy requirements first (Docker caching optimization)
# If requirements don't change, Docker reuses this layer = faster builds
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir reduces image size by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into container
COPY app/ /app/

# Create exports directory for saved designs
RUN mkdir -p /app/exports

# Expose port 5000 (Flask's default port)
# This tells Docker which port the app uses
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=main.py

# Command to run when container starts
# 0.0.0.0 allows external access (not just localhost)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "main:app"]
