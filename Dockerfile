FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 8000 (Azure Web Apps uses 8000 by default for containers)
EXPOSE 8000

# Start Flask app using gunicorn
CMD ["unicorn", "--bind", "0.0.0.0:8000", "app:app"]