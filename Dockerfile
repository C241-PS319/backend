# Use the official Python image as the base image
FROM python:3.9-slim

# Menggunakan variabel lingkungan sebagai build argument
ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG SECRET_KEY
ARG ENVIRONMENT
ARG FIREBASE_SERVICE_ACCOUNT
ARG WEATHER_API_KEY
ARG EMAIL_HOST
ARG EMAIL_HOST_USER
ARG EMAIL_HOST_PASSWORD
ARG DEFAULT_FROM_EMAIL

# Set nilai variabel lingkungan dalam lingkungan Docker
ENV DATABASE_NAME=$DATABASE_NAME
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_PORT=$DATABASE_PORT
ENV SECRET_KEY=$SECRET_KEY
ENV ENVIRONMENT=$ENVIRONMENT
ENV FIREBASE_SERVICE_ACCOUNT=$FIREBASE_SERVICE_ACCOUNT
ENV WEATHER_API_KEY=$WEATHER_API_KEY
ENV EMAIL_HOST=$EMAIL_HOST
ENV EMAIL_HOST_USER=$EMAIL_HOST_USER
ENV EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD
ENV DEFAULT_FROM_EMAIL=$DEFAULT_FROM_EMAIL

# Set the working directory in the container
WORKDIR /docker-app

# Copy the requirements file into the container at /docker-app
COPY requirements.txt /docker-app/

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /docker-app
COPY . /docker-app/

# Expose port 8000 to the outside world
EXPOSE 8000
EXPOSE 443
EXPOSE 2525

# Collect static for better visualization
RUN python manage.py collectstatic

# Run migrate DB
RUN python manage.py migrate

# Jalankan Gunicorn
CMD ["gunicorn", "app.patera.wsgi", "--bind", "0.0.0.0:8000", "--bind", "0.0.0.0:443", "--certfile=/home/node/app/cert/server.cert", "--keyfile=/home/node/app/cert/server.key"]