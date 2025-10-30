from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.NoteModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "createdAt", "updatedAt"]
