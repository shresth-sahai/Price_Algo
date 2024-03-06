# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your Python files into the container
COPY . .

# Run your Python script
CMD ["python", "test.py"]