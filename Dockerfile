# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (including Tesseract if needed)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set environment variables
ENV PORT=7860

# Expose port
EXPOSE 7860

# Start server
CMD ["gunicorn", "backend.server.main:app", "--bind", "0.0.0.0:7860", "--workers", "2"]
