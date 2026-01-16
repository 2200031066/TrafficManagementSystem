# Backend Dockerfile for Traffic Management System
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    cmake \
    wget \
    libopencv-dev \
    python3-opencv \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Compile C++ Genetic Algorithm
RUN g++ -std=c++17 -O3 -march=native -fopenmp -o Algo1 Algo.cpp

# Create necessary directories with proper permissions
RUN mkdir -p uploads outputs data && \
    chmod 777 uploads outputs data

# Create non-root user matching host UID
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Note: Running as root to handle volume mount permissions
# The app will handle directory permissions at runtime
USER root

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Run the application
CMD ["./entrypoint.sh"]
