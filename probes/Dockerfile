# Use the official Python image
FROM python:3.10-alpine

# Install Flask
RUN pip install Flask

# Copy the application code
COPY . /probe_app

# Set the working directory
WORKDIR /probe_app

# Run the application
CMD ["python", "probe_app.py"]
