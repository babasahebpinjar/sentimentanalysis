# Use the Python image form ECR as a parent image
FROM public.ecr.aws/docker/library/python:3.9-slim-buster
# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "app.py"]

