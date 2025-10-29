from ToDo.models import ToDoModel

def patch_all(status):
    if not isinstance(status, bool):
        return {"success": False, "statusCode": 0, "message": "Must be False or True!"}
    ToDoModel.objects.update(status=status)
    return {"success": True, "statusCode": 1, "message": "Success"}

def patch_single_status(status, id):
    if not isinstance(status, bool):
        return {"success": False, "statusCode": 0, "message": "Status must be False or True!"}
    elif not isinstance(id, int):
        return {"success": False, "statusCode": 0, "message": "ID must be int!"}
    try:
        todo_item = ToDoModel.objects.get(id=id)
        todo_item.status = status
        todo_item.save()
        return {"success": True, "statusCode": 1, "message": "Success"}
    except ToDoModel.DoesNotExist:
        return {"success": False, "statusCode": 0, "message": "Item not found"}

def patch_single_text(text, id):
    if not isinstance(text, str):
        return {"success": False, "statusCode": 0, "message": "Text must be string!"}
    elif not isinstance(id, int):
        return {"success": False, "statusCode": 0, "message": "ID must be int!"}
    try:
        todo_item = ToDoModel.objects.get(id=id)
        todo_item.text = text
        todo_item.save()
        return {"success": True, "statusCode": 1, "message": "Success"}
    except ToDoModel.DoesNotExist:
        return {"success": False, "statusCode": 0, "message": "Item not found"}
