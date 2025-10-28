from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.ToDo.as_view())
]