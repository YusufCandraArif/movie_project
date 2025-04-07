# Use official Python image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy project
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run migrations and load data
RUN python manage.py migrate
RUN python manage.py load_movies

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
