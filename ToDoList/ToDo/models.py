from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=127)
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)