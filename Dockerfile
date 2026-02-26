# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Create virtual environment and install dependencies
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r requirements.txt

# Copy all project files (including data folder)
COPY . .

# Set PATH to use the venv by default
ENV PATH="/opt/venv/bin:$PATH"

# Default command to run tests inside the venv
CMD ["pytest", "-m","smoke"]