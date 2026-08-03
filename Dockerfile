# Use the latest Python slim image with pinned digest
FROM python:3.14.3-slim@sha256:6a27522252aef8432841f224d9baaa6e9fce07b07584154fa0b9a96603af7456

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
