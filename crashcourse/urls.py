from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from crashcourse.views import list_all, get_db_as_json
from django.contrib.auth.views import LoginView, LogoutView
from .views import  SignupView
urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('signup/', SignupView.as_view(), name='signup'),

	path('admin/', admin.site.urls),

	path('', list_all),
	path('todo/', include('todo.urls', namespace="todo")),
	path('note/', include('note.urls', namespace="note")),
	path('bookmark/', include('bookmark.urls', namespace="bookmark")),
	path('getdb/', get_db_as_json, name="export-user-db"),

]
if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)