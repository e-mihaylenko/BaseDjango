from Note.models import NoteModel


def post_into_model(title, content):
    if title is None:
        return {"success": False, "statusCode": 0, "massage": "Title not found!"}
    elif content is None:
        return {"success": False, "statusCode": 0, "massage": "Title not found!"}
    note = NoteModel.objects.create(title=title, content=content)
    note_data = {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "createdAt": note.createdAt,
        "updatedAt": note.updatedAt,
    }
    response = {
        "success": True,
        "statusCode": 1,
        "message": "Success",
        "data": note_data,
    }
    return response
