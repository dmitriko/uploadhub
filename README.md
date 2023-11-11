# UploadHub

## Overview
UploadHub is a minimalistic Django application designed for uploading files to an S3-compatible storage service. It provides a simple web interface for uploading files and handles each file with a unique identifier to avoid conflicts. The app also supports password-protected access. It will be a bit of a challenge to put it to Kubernetes. Thus it is a perfect app to exersice our DevOps skills.

## Features
- File upload to S3 with unique UUIDs for each file.
- Password protection for accessing the upload interface.
- List and delete functionality for uploaded files.
- Simple integration with S3-compatible services like AWS S3 and MinIO.
- Designed to be run on Kubernetes, fitting well into a DevOps learning curriculum.

## Prerequisites
- Python 3.8 or higher.
- Django 3.2 or higher.
- An S3-compatible storage service (e.g., AWS S3, MinIO).
- Docker and Kubernetes for containerization and orchestration.

## Local Development Setup
To start the application locally, run the following command:

```bash
docker compose up
```
This command will build the Docker images and start the services defined in compose.yaml, which are django, postgres and minio

## Kubernetes
As part of our DevOps training, we will employ Terraform to establish foundational infrastructure. Subsequently, we will craft a Helm Chart to streamline the deployment of our application. This hands-on approach ensures a practical understanding of managing and deploying applications in a Kubernetes environment.
