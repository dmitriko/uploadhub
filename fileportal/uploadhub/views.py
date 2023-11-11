from django.shortcuts import render
from django.core.files.storage import default_storage

def index(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        # Add additional code here to handle the uploaded file

    return render(request, 'index.html')
