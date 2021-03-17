from django.urls import path

from todo.views import todo_detail, todo_create, todo_update, todo_delete, todo_check

app_name = 'todo'

urlpatterns = [
	path('create/', todo_create, name="create"),
	path('<id>/', todo_detail, name="detail"),
	path('<id>/update/', todo_update, name="update"),
	path('<id>/delete/', todo_delete, name="delete"),
	path('<id>/check/', todo_check, name="check"),
]
