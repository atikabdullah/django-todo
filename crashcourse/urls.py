from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from crashcourse.views import list_all, get_db_as_json

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', list_all),
	path('todo/', include('todo.urls', namespace="todo")),
	path('note/', include('note.urls', namespace="note")),
	path('bookmark/', include('bookmark.urls', namespace="bookmark")),
	path('getdb/', get_db_as_json),

]
if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)