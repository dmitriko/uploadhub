from django.db import models
import uuid

class UploadedFile(models.Model):
    original_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)
    unique_id = models.UUIDField(default=uuid.uuid4, 
                                 editable=False, 
                                 unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
