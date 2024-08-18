# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables

# Collect static files (uncomment if you have static files to collect)
# RUN python manage.py collectstatic --noinput

# Run migrations (uncomment if you want to run migrations automatically)
RUN python manage.py migrate

# Run the Django app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "hospital.wsgi:application"]
