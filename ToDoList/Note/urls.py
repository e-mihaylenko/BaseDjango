from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.Notes.as_view()),
    path('notes/<int:id>', views.notes_id.as_view())
]
