# Dockerfile (Flask Backend)

# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY .\ .

# Expose port for development
EXPOSE 3002

# Run command to start development server
CMD ["python", "app.py"]