# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory in the container
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the application runs on
EXPOSE 8000

# Run migrations and collect static files
# RUN python manage.py makemigrations
# RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Create a superuser
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'mohammadmasoudie@gmail.com', 'The.miiim48836083')" | python manage.py shell

# Define the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
