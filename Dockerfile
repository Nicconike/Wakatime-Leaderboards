# Use the latest Python slim image with pinned digest
FROM python:3.13.5-slim@sha256:83c04b3d51c2150e7d23f6f2911059e7f1a5a4ff8870ef6eb7d4ea4ac6b49638

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
