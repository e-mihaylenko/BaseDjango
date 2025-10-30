from Note.models import NoteModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_from_note(page, size):
    note = NoteModel.objects.all()
    paginator = Paginator(note, size)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    data = []
    for item in post:
        data.append(
            {
                "id": item.id,
                "title": item.title,
                "content": item.content,
                "createdAt": item.createdAt,
                "updatedAt": item.updatedAt,
            }
        )
    response = {"success": True, "statusCode": 1, "message": "Success", "data": data}
    return response


def get_id(id):
    if not isinstance(id, int):
        return {"success": False, "statusCode": 0, "massage": "ID must be integer!"}
    try:
        note = NoteModel.objects.get(id=id)
        return {"success": True, "statusCode": 1, "massage": "Success", "data": note}
    except NoteModel.DoesNotExist:
        return {"success": False, "statusCode": 0, "massage": "ID not found!"}
