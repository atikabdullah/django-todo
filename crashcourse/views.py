from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from queryset_sequence import QuerySetSequence

from bookmark.models import Bookmark
from note.models import Note
from todo.models import Todo


def list_all(request):
	queryset = list()
	todos = Todo.objects.all() if request.GET.get('todos') == 'true' else None
	notes = Note.objects.all() if request.GET.get('notes') == 'true' else None
	bookmarks = Bookmark.objects.all() if request.GET.get('bookmarks') == 'true' else None
	date_sort: bool = not request.GET.get('date-sort')  # Switch
	search = request.GET.get('search') if request.GET.get('search') is not None else ''
	toggle_viewtype = True if request.GET.get('toggle-viewtype') == 'true' else False

	for item in [todos, notes, bookmarks]:
		if item is not None:
			queryset.append(item)

	if len(queryset) == 1:
		all_items = QuerySetSequence(queryset[0]).order_by('-date_created' if date_sort else 'date_created').filter(Q(name__contains=search) | Q(description__contains=search))
	elif len(queryset) == 2:
		all_items = QuerySetSequence(queryset[0], queryset[1]).order_by('-date_created' if date_sort else 'date_created').filter(Q(name__contains=search) | Q(description__contains=search))
	elif len(queryset) == 3:
		all_items = QuerySetSequence(queryset[0], queryset[1], queryset[2]).order_by('-date_created' if date_sort else 'date_created').filter(Q(name__contains=search) | Q(description__contains=search))
	else:
		all_items = QuerySetSequence(Todo.objects.all(), Note.objects.all(), Bookmark.objects.all()).order_by('-date_created' if date_sort else 'date_created').filter(Q(name__contains=search) | Q(description__contains=search))

	paginator = Paginator(all_items, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		"page_obj": page_obj,
		"date_sort": date_sort,
		"todos" : 'true' if todos else 'false',
		"notes" : 'true' if notes else 'false',
		"bookmarks" : 'true' if bookmarks else 'false',
		"listview" : 'true' if toggle_viewtype else 'false',

	}
	site = "index.html" if toggle_viewtype is False else "index-table.html"
	return render(request, site, context)
