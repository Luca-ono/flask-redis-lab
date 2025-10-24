# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt (if you had one)
# Since you don't have one, we just install Flask directly
RUN pip install Flask
RUN pip install redis 

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Optional: Set environment to development for debugging, remove for production
ENV FLASK_ENV=development

# Run app.py when the container launches using Flask's built-in server
CMD ["flask", "run"]