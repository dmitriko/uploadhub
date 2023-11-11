FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /opt/fileportal

# Install dependencies
COPY requirements.txt /opt/fileportal/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /opt/fileportal
# COPY ./fileportal /opt/fileportal/
