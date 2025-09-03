# Use an official python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install all libraries
RUN pip install -r requirements.txt

# make port 8080 available to the world outside the container
EXPOSE 8080

# Define environment variable to ensure Flask runs in production mode
ENV FLASK_ENV=production

CMD ["python3", "app.py"]