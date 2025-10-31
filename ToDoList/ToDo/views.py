from django.views import View
from django.http import JsonResponse, HttpRequest
from .requests import todo_post, todo_get, todo_patch
import django.middleware.csrf as dj_csrf
import django.views.decorators.http as dj_decorator_http
import json

from . import models


@dj_decorator_http.require_GET
def get_csrf(request: HttpRequest):
    return JsonResponse({"csrfToken": dj_csrf.get_token(request)})


class ToDo(View):
    def post(self, request):
        txt = json.loads(request.body)
        text = txt.get("text")
        response = todo_post.post_into_todo(text)

        return JsonResponse(response)

    def get(self, request):
        page = request.GET.get("page", 1)
        per_page = request.GET.get("perPage", 10)
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
        return JsonResponse({"success": True, "statusCode": 1, "message": "Success"})


class status_id_todo(View):
    def patch(self, request, id):
        try:
            data = json.loads(request.body)
            status = data["status"]
            response = todo_patch.patch_single_status(status, id)

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
            response = todo_patch.patch_single_text(text, id)

            return JsonResponse(response)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse(
                {
                    "success": False,
                    "statusCode": 0,
                    "message": "Invalid JSON or missing 'text' field",
                }
            )
