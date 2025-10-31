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
                "createdAt": item.createdAt.isoformat(),
                "updatedAt": item.updatedAt.isoformat(),
            }
        )
    response = {"success": True, "statusCode": 1, "message": "Success", "data": data}
    return response


def get_id(id):
    try:
        note = NoteModel.objects.get(id=id)
        data = {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "createdAt": note.createdAt.isoformat(),
            "updatedAt": note.updatedAt.isoformat(),
        }
        return {"success": True, "statusCode": 1, "message": "Success", "data": data}
    except NoteModel.DoesNotExist:
        return {"success": False, "statusCode": 0, "message": "ID not found!"}
