from django.urls import path

from .views import note_detail, note_create, note_update, note_delete, note_list

app_name = 'note'

urlpatterns = [
	path('', note_list, name="list"),
	path('create/', note_create, name="create"),
	path('<id>/', note_detail, name="detail"),
	path('<id>/update/', note_update, name="update"),
	path('<id>/delete/', note_delete, name="delete"),
]
