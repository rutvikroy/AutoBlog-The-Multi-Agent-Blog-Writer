FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system packages
RUN apt update -y && apt install -y azurecli && apt clean

# Set working directory
WORKDIR /app

# Copy all files (including main.py, requirements.txt, etc.)
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080

# Start the app and bind to all interfaces
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]