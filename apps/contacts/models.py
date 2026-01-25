from django.db import models

from apps.charity.models import BaseModel

class Subject(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
