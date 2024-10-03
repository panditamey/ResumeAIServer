# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first (if you have it for dependencies)
COPY requirements.txt ./

# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 (or any port your app runs on, adjust if needed)
EXPOSE 5000

# Run the server.py using Python
CMD ["python", "./server.py"]
