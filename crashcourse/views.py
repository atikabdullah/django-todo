from itertools import chain

from django.core.paginator import Paginator
from django.shortcuts import render

from bookmark.models import Bookmark
from note.models import Note
from todo.models import Todo


def list_all(request):
	todos = Todo.objects.all()
	notes = Note.objects.all()
	bookmarks = Bookmark.objects.all()
	all_items = list(chain(bookmarks, notes, todos))
	paginator = Paginator(all_items, 5)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		"page_obj": page_obj,

	}
	return render(request, "index.html", context)
