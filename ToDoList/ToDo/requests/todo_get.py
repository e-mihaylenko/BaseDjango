from ToDo.models import ToDoModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_from_todo(page, per_page, status):
    todos = ToDoModel.objects.all()
    if status is not None:
        if status.lower() == "true":
            todos = todos.filter(status=True)
        elif status.lower() == "false":
            todos = todos.filter(status=False)
    paginator = Paginator(todos, per_page)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    content = []
    for item in post:
        content.append(
            {
                "id": item.id,
                "text": item.text,
                "status": item.status,
                "createdAt": item.createdAt,
                "updatedAt": item.updatedAt,
            }
        )
    response = {
        "content": content,
        "pageNumber": post.number - 1,
        "pageSize": per_page,
        "totalPages": paginator.num_pages,
        "totalElements": paginator.count,
    }

    return response
