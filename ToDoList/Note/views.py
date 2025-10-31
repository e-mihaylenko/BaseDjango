from django.views import View
from django.http import JsonResponse
import json

from .requests import note_post, note_get, note_patch
from .models import NoteModel


# Create your views here.
class Notes(View):
    def post(self, request):
        data = json.loads(request.body)
        title = data.get("title", None)
        content = data.get("content", None)
        response = note_post.post_into_model(title, content)
        return JsonResponse(response)

    def get(self, request):
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 10)
        response = note_get.get_from_note(page, size)
        return JsonResponse(response)


class notes_id(View):
    def get(self, request, id):
        response = note_get.get_id(id)
        return JsonResponse(response)

    def patch(self, request, id):
        data = json.loads(request.body)
        response = note_patch.patch_id(data["title"], data["content"], id)
        return JsonResponse(response)

    def delete(self, request, id):
        if not isinstance(id, int):
            return JsonResponse(
                {"success": False, "statusCode": 0, "message": "ID must be integer!"}
            )
        try:
            NoteModel.objects.filter(id=id).delete()
            return JsonResponse({"success": True, "statusCode": 1, "message": "Success"})
        except NoteModel.DoesNotExist:
            return JsonResponse({"success": False, "statusCode": 0, "message": "Item not found!"})
