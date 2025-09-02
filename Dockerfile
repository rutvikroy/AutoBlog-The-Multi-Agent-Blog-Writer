FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000  
# Azure/Heroku-friendly

# Install system packages
RUN apt update -y && apt install -y azure-cli && apt clean

# Copy dependency files first (so pip can see setup.py if -e . is in requirements.txt)
COPY requirements.txt setup.py ./

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port 8000 (Azure Web Apps uses 8000 by default for containers)
EXPOSE 8000

# Start Flask app using uvicorn
CMD ["uvicorn", "--bind", "0.0.0.0:8000", "app:app"]
