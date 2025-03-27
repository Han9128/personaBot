# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak-ng \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for web traffic
EXPOSE 8000

# Define environment variable
# (You can remove this if not necessary)
ENV NAME World

# Run the application using gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "Backend.server:app"]
