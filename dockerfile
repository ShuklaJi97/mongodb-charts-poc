FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY mongodb_data_generator.py .
COPY examples/ ./examples/
COPY tests/ ./tests/

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD python -c "import pymongo; print('Health check passed')" || exit 1

# Default command
CMD ["python", "mongodb_data_generator.py"]

# Labels for metadata
LABEL maintainer="your-email@example.com"
LABEL version="1.0.0"
LABEL description="MongoDB Atlas Charts POC Data Generator"
LABEL org.opencontainers.image.source="https://github.com/yourusername/mongodb-charts-poc"