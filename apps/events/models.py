from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_editorjs_fields import EditorJsJSONField
from stdimage import StdImageField

from apps.charity.models import BaseModel, City
from apps.charity.utils import UploadToPathAndRename


class Event(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = StdImageField(
        upload_to=UploadToPathAndRename('image'),
        variations={
            'large': (600, 400, True),
            'thumbnail': (300, 200, True),
            'icon': (70, 70, True)
        },
        null=True,
        blank=True,
        delete_orphans=True
    )
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField(default=timezone.now)
    event_start_time = models.TimeField(default=timezone.now)
    event_end_time = models.TimeField(default=timezone.now)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    content = EditorJsJSONField(blank=True, null=True)

    @property
    def is_upcoming(self):
        return self.event_date >= timezone.now()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug})
