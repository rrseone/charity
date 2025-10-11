from django.db import models
from django_editorjs_fields import EditorJsJSONField


class Page(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=False, null=True)
    content = EditorJsJSONField(blank=True, null=True)

    def __str__(self):
        return self.title
