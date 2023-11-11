import uuid
import boto3
import os
import logging


from django.core.files.storage import default_storage
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UploadedFile 


def index(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        unique_id = uuid.uuid4()
        file_name = f"{unique_id}"
        content_type = file.content_type

        # Save file to S3
        default_storage.save(file_name, file)

        # Save file details to the database
        UploadedFile.objects.create(original_name=file.name, unique_id=unique_id, content_type=content_type)

    # Fetch list of files from the database
    files = UploadedFile.objects.all()
    return render(request, 'index.html', {'files': files})


def delete_file(request, unique_id):
    if request.method == 'POST':
        file_to_delete = UploadedFile.objects.get(unique_id=unique_id)
        s3_client_kwargs = {}
        if os.environ.get('USE_MINIO', 'False').lower() == 'true':
            logging.info('Using MinIO')
            s3_client_kwargs['endpoint_url'] = os.environ['AWS_S3_ENDPOINT_URL']
            s3_client_kwargs['aws_access_key_id'] = os.environ['AWS_ACCESS_KEY_ID']
            s3_client_kwargs['aws_secret_access_key'] = os.environ['AWS_SECRET_ACCESS_KEY']
            s3_client_kwargs['region_name'] = os.environ['AWS_S3_REGION_NAME']
            s3_client_kwargs['verify'] = False  # May be needed if MinIO uses self-signed certificates

        s3 = boto3.client('s3', **s3_client_kwargs)
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME 
        s3.delete_object(Bucket=bucket_name, Key=str(file_to_delete.unique_id))
        file_to_delete.delete()

        return HttpResponseRedirect(reverse('index'))

