from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ToDoModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "text", "createdAt", "updatedAt"]
