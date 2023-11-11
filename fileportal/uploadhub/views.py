import uuid
import boto3

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
        s3 = boto3.client('s3')
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME 
        s3.delete_object(Bucket=bucket_name, Key=str(file_to_delete.unique_id))
        file_to_delete.delete()

        return HttpResponseRedirect(reverse('index'))

