from ToDo.models import ToDoModel


def post_into_todo(text):
    if not text:
        return {"success": False, "massage": "Text not found!", "status": 400}
    element = ToDoModel.objects.create(text=text)
    task_data = {
        "id": element.id,
        "text": element.text,
        "status": element.status,
        "createdAt": element.createdAt,
        "updatedAt": element.updatedAt,
    }
    response = {
        "success": True,
        "statusCode": 1,
        "message": "Success",
        "data": task_data,
    }

    return response
