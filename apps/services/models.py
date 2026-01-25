from django.db import models
from django.urls import reverse
from django_editorjs_fields import EditorJsJSONField

from apps.charity.models import BaseModel
from apps.charity.utils import UploadToPathAndRename


class Service(BaseModel):
    is_featured = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to=UploadToPathAndRename('images'), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = EditorJsJSONField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})
