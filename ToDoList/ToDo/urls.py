from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.ToDo.as_view()),
    path('todo/status/<int:id>', views.status_id_todo.as_view()),
    path('todo/text/<int:id>', views.text_id_todo.as_view()),
    path("get-csrf", views.get_csrf,name="Get csrf key")
]
