# Use official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Django runs on
EXPOSE 8000

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
