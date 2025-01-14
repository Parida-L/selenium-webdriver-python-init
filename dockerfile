# Base image with Python
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrandr2 \
    xdg-utils \
    libatk1.0-0 \
    libgbm-dev \
    fonts-liberation \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Hardcoded ChromeDriver version compatible with Chromium 131.0.6778.264
ENV CHROMEDRIVER_VERSION=114.0.5735.90

# Install ChromeDriver
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Set environment variables for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/local/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Command to run tests
CMD ["pytest", "--html=report.html"]
