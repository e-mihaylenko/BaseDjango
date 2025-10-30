from Note.models import NoteModel

def patch_id(title, content, id):
    if not isinstance(title, str):
        return {"success": False, "statusCode": 0, "massage": "Title must be string!"}
    elif not isinstance(content, str):
        return{"success": False, "statusCode": 0, "massage": "Content must be string!"}
    elif not isinstance(id, int):
        return {"success": False, "statusCode": 0, "massage": "ID must be integer!"}
    try:
        note = NoteModel.objects.filter(id=id).update(title=title, content=content)
        return {
        "success": True,
        "statusCode": 1,
        "message": "Success",
        "data": note
    }
    except NoteModel.DoesNotExist:
        return {"success": False, "statusCode": 0, "massage": "Item not found!"}
