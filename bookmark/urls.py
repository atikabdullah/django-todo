from django.urls import path

from bookmark.views import bookmark_detail, bookmark_create, bookmark_update, bookmark_delete, bookmark_list

app_name = 'bookmark'

urlpatterns = [
	path('', bookmark_list, name="list"),
	path('create/', bookmark_create, name="create"),
	path('<id>/', bookmark_detail, name="detail"),
	path('<id>/update/', bookmark_update, name="update"),
	path('<id>/delete/', bookmark_delete, name="delete"),
]
