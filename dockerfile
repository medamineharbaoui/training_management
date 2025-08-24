FROM python:3.11-slim

# Install system dependencies for MySQL/MariaDB client
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev libmariadb-dev build-essential pkg-config && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements first to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Make wait-for-it.sh executable inside the container
RUN ["chmod", "+x", "wait-for-it.sh"]

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
