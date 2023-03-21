FROM python:3.9-slim-buster

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables
ENV FLASK_APP=subscription_service.py
ENV FLASK_ENV=production
ENV DATABASE_URL=postgresql://user:password@db_host:5432/db_name

# Expose the port that the microservice will listen on
EXPOSE 5000

# Start the microservice
CMD ["flask", "run", "--host=0.0.0.0"]
