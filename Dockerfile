FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000  
# Azure/Heroku-friendly

#Set working directory
WORKDIR /app

# Install system packages (optional: remove azure-cli if not needed in container)
RUN apt-get update -y && apt-get install -y --no-install-recommends azure-cli && \
    rm -rf /var/lib/apt/lists/*

#Copy application code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (Azure Web Apps uses 8000 by default for containers)
EXPOSE 8000

# Start Flask app using uvicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
