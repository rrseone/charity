from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_editorjs_fields import EditorJsJSONField
from stdimage import StdImageField

from apps.base.models import BaseModel
from apps.base.utils import UploadToPathAndRename


class Campaign(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    content = EditorJsJSONField(null=True, blank=True)
    image = StdImageField(
        upload_to=UploadToPathAndRename('image'),
        variations={
            'large': (600, 400, True),
            'thumbnail': (380, 250, True),
            'icon': (80, 80, True),
        },
        blank=True,
        null=True,
        delete_orphans=True,
    )
    raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    goal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('campaigns:campaign_detail', kwargs={'slug': self.slug})

    def get_raised_percentage(self):
        return round((self.raised / self.goal) * 100)
