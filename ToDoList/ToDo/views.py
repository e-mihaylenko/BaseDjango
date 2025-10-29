from django.views import View
from django.http import JsonResponse
from .requests import todo_post, todo_get, todo_patch
import json
from . import models


class ToDo(View):
    def post(self, request):
        txt = json.loads(request.body)
        text = txt.get("text")
        response = todo_post.post_into_todo(text)

        return JsonResponse(response)

    def get(self, request):
        page = request.GET.get("page", 1)
        per_page = request.GET.get("perPage", 1)
        status = request.GET.get("status", None)
        response = todo_get.get_from_todo(page, per_page, status)

        return JsonResponse(response)

    def patch(self, request):
        try:
            data = json.loads(request.body)
            status = data["status"]
            response = todo_patch.patch_all(status)

            return JsonResponse(response)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse(
                {
                    "success": False,
                    "statusCode": 0,
                    "message": "Invalid JSON or missing 'status' field",
                }
            )

    def delete(self, request):
        models.ToDoModel.objects.filter(status=True).delete()
        return JsonResponse({
            "success": True,
            "statusCode": 1,
            "message": "Success"
            })

class status_id_todo(View):
    def patch(self, request, id):
        try:
            data = json.loads(request.body)
            status = data["status"]
            response = todo_patch.patch_single(status, id)

            return JsonResponse(response)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse(
                {
                    "success": False,
                    "statusCode": 0,
                    "message": "Invalid JSON or missing 'status' field",
                }
            )

class text_id_todo(View):
    def patch(self, request, id):
        try:
            data = json.loads(request.body)
            text = data["text"]
            response = todo_patch.patch_single_status(text, id)

            return JsonResponse(response)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse(
                {
                    "success": False,
                    "statusCode": 0,
                    "message": "Invalid JSON or missing 'text' field",
                }
            )
