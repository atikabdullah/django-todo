from django.urls import path

from todo.views import todo_list, todo_detail, todo_create, todo_update, todo_delete, todo_check

app_name = 'todo'

urlpatterns = [
	path('', todo_list),
	path('create/', todo_create),
	path('<id>/', todo_detail),
	path('<id>/update/', todo_update),
	path('<id>/delete/', todo_delete),
	path('<id>/check/', todo_check),
]
