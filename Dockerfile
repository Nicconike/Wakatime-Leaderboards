# Use the latest Python slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/wakatime-leaderboards
ENV HOME=/wakatime-leaderboards

# Create a non-root user with explicit UID/GID
RUN groupadd -g 10001 appgroup && \
    useradd -u 10000 -g appgroup -d /wakatime-leaderboards appuser && \
    mkdir -p /wakatime-leaderboards && \
    chown -R appuser:appgroup /wakatime-leaderboards

# Set the working directory in the container
WORKDIR /wakatime-leaderboards

# Copy the requirements file into the container
COPY --chown=appuser:appgroup requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code with proper ownership
COPY --chown=appuser:appgroup api/ ./api/

# Switch to non-root user
USER appuser

# Set the entrypoint to run the Python script
ENTRYPOINT ["sh", "-c", "cd /wakatime-leaderboards && python api/main.py"]
