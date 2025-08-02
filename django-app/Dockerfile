# Use Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better for caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . /app/

# Expose the Django default port
EXPOSE 8000

# Run the app with gunicorn
#CMD ["gunicorn", "django_app.wsgi:application", "--bind", "0.0.0.0:8000"]

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
