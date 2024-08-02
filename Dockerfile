# Use the latest Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/wakatime-leaderboards

# Set the working directory in the container
WORKDIR /wakatime-leaderboards

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and other necessary files into the container
COPY api/ ./api/

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "api/main.py"]
