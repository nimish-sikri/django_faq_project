# Use the official Python image as base
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
# COPY . /app/
COPY . . 

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt
# COPY ./faq_project /app/faq_project
# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
# Collect static files (if needed)
# RUN python manage.py collectstatic --noinput
RUN python faq_project/manage.py collectstatic --noinput

# Expose the port that the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_project.wsgi:application"]
