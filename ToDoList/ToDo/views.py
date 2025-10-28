from django.views import View
from django.http import JsonResponse
from .requests import todo_post
import json

class ToDo(View):
    def post(self, request):
        txt = json.loads(request.body)
        text = txt.get("text")
        response = todo_post.post_into_todo(text)

        return JsonResponse(response)


    def get(self, request):
        return JsonResponse({"2":"Hello, world!"})
