from django.contrib import admin
from django.urls import path, include

from crashcourse.views import list_all

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', list_all),
	path('todo/', include('todo.urls', namespace="todo")),
	path('note/', include('note.urls', namespace="note")),
	path('bookmark/', include('bookmark.urls', namespace="bookmark")),
]
