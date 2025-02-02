# Use the latest Python slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/wakatime-leaderboards \
    HOME=/wakatime-leaderboards

# Create non-root user with explicit UID/GID
RUN groupadd -g 10001 appgroup && \
    useradd -u 10000 -g appgroup \
    --create-home --home-dir "$HOME" \
    --shell /bin/false appuser

# Set working directory
WORKDIR $HOME

# Copy requirements.txt with root ownership and read-only permissions
COPY --chmod=644 requirements.txt .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chmod=644 api/ ./api/

# Explicit permission setup
RUN chown -R appuser:appgroup "$HOME" && \
    find "$HOME" -type d -exec chmod 755 {} \; && \
    find "$HOME" -type f -exec chmod 644 {} \;

# Switch to non-root user
USER appuser

# Set the entrypoint to run the Python script
ENTRYPOINT ["sh", "-c", "cd /wakatime-leaderboards && python api/main.py"]
