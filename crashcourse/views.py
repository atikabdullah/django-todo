from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from queryset_sequence import QuerySetSequence

from bookmark.models import Bookmark
from note.models import Note
from todo.models import Todo


def list_all(request):
	queryset = list()
	todos = Todo.objects.all() if request.GET.get('todos') == 'true' else None
	notes = Note.objects.all() if request.GET.get('notes') == 'true' else None
	bookmarks = Bookmark.objects.all() if request.GET.get('bookmarks') == 'true' else None
	date_sort = 'true' if request.GET.get('datesort') == 'true' else 'false'
	search = request.GET.get('search') if request.GET.get('search') is not None else ''
	toggle_viewtype = True if request.GET.get('toggle_viewtype') == 'true' else False

	for item in [todos, notes, bookmarks]:
		if item is not None:
			queryset.append(item)

	all_items = QuerySetSequence(*queryset).order_by('-date_created' if date_sort == 'true' else 'date_created').filter(Q(name__contains=search) | Q(description__contains=search))

	paginator = Paginator(all_items, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.POST:
		todos = request.POST.get('todos')
		notes = request.POST.get('notes')
		bookmarks = request.POST.get('bookmarks')
		page = request.POST.get('page')
		toggle_viewtype = request.POST.get('toggle_viewtype')
		datesort = request.POST.get('datesort')
		page= page_obj.number
		search = request.POST.get('search')
		parameterized_url = f"/?search={search}&todos={todos}&notes={notes}&bookmarks={bookmarks}&toggle_viewtype={toggle_viewtype}&datesort={datesort}&page={page}"

		return redirect(parameterized_url)

	context = {
		"page_obj": page_obj,
		"datesort": date_sort,
		"todos": 'true' if todos else 'false',
		"notes": 'true' if notes else 'false',
		"bookmarks": 'true' if bookmarks else 'false',
		"toggle_viewtype": 'true' if toggle_viewtype else 'false',

	}
	site = "index.html" if toggle_viewtype is False else "index-table.html"
	return render(request, site, context)
