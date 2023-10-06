# Use an official Python runtime as a parent image
FROM python:3.8-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mysite.settings

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

