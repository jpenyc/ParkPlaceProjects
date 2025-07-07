# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Command to run the application using Gunicorn
# We'll run migrations first, then start Gunicorn
# This is a simplified approach for development; for production, migrations
# are usually run as a separate step before starting the app servers.
CMD ["sh", "-c", "python manage.py migrate && gunicorn home_projects.wsgi:application --bind 0.0.0.0:8000"]
