# Use the latest Python slim image with pinned digest
FROM python:3.14.2-slim@sha256:9b81fe9acff79e61affb44aaf3b6ff234392e8ca477cb86c9f7fd11732ce9b6a

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/wakatime-leaderboards

# Create non-root user with explicit UID
RUN useradd -u 10000 -ms /bin/bash wakatime-leaderboards

# Set working directory
WORKDIR /wakatime-leaderboards

# Copy project files
COPY . .

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -e . && \
    apt-get purge -y --auto-remove git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    chown -R wakatime-leaderboards:wakatime-leaderboards /wakatime-leaderboards/

# Switch to non-root user
USER wakatime-leaderboards

# Set the entrypoint
ENTRYPOINT ["python", "-m", "api.main"]
