from django.db import models


# Create your models here.
class NoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127)
    content = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
