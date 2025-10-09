# Use the latest Python slim image with pinned digest
FROM python:3.14.0-slim@sha256:1e7c3510ceb3d6ebb499c86e1c418b95cb4e5e2f682f8e195069f470135f8d51

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
