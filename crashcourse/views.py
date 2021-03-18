from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from queryset_sequence import QuerySetSequence

from bookmark.models import Bookmark
from note.models import Note, Tag
from todo.models import Todo


def flip(stringbool):
	if stringbool == 'true':
		return 'false'
	elif stringbool == 'false':
		return 'true'
	else:
		return 'false'


def set_session(request):
	todos = request.session['todos'] = 'true'
	notes = request.session['notes'] = 'true'
	bookmarks = request.session['bookmarks'] = 'true'
	sortbydate = request.session['sortbydate'] = 'false'
	toggle_viewtype = request.session['toggle_viewtype'] = 'false'
	search = request.session['search'] = ''
	request.session['url_parameters'] = f"/?search={search}&todos={todos}&notes={notes}&bookmarks={bookmarks}&toggle_viewtype={toggle_viewtype}&sortbydate={sortbydate}"
	return request


def update_session(request):
	todos = request.session['todos'] = request.POST.get('todos')
	notes = request.session['notes'] = request.POST.get('notes')
	bookmarks = request.session['bookmarks'] = request.POST.get('bookmarks')
	sortbydate = request.session['sortbydate'] = request.POST.get('sortbydate')
	toggle_viewtype = request.session['toggle_viewtype'] = request.POST.get('toggle_viewtype')
	if request.POST.get('reset') != 'true':
		search = request.session['search'] = request.POST.get('search')
	else:
		search = request.session['search'] = ''
	request.session['url_parameters'] = f"/?search={search}&todos={todos}&notes={notes}&bookmarks={bookmarks}&toggle_viewtype={toggle_viewtype}&sortbydate={sortbydate}"
	return request


def compare_session_value(request, variable, true):
	if request.session.get(variable) == str(true):
		return 'true'
	else:
		return 'false'


def list_all(request):
	queryset = list()

	if request.session.get('url_parameters') is None:
		request = set_session(request)
		redirect('/')
	# redirect(request.session.get('url_parameters'))

	if request.POST:
		request = update_session(request)
		if request.POST.get("cleartags") == 'true':
			return HttpResponseRedirect(redirect_to='/')
		redirect('/')
	# return redirect(request.session.get('url_parameters'))

	todos = Todo.objects.all() if compare_session_value(request, 'todos', 'true') == 'true' else None
	notes = Note.objects.all() if compare_session_value(request, 'notes', 'true') == 'true' else None
	bookmarks = Bookmark.objects.all() if compare_session_value(request, 'bookmarks', 'true') == 'true' else None
	tags = Tag.objects.all()
	tag_quantities = Note.objects.values_list('tags__name').annotate(c=Count('tags__name')).order_by('-c')

	if request.GET.get("tags") and notes is not None:
		notes = notes.filter(tags__name__in=[request.GET.get("tags")])

	for item in [todos, notes, bookmarks]:
		if item is not None:
			queryset.append(item)

	all_items = QuerySetSequence(*queryset). \
		order_by('-date_created' if request.session.get('sortbydate') == 'true' else 'date_created'). \
		filter(Q(name__contains=request.session.get('search')) | Q(description__contains=request.session.get('search')))

	paginator = Paginator(all_items, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		"page_obj": page_obj,
		"sortbydate": request.session.get('sortbydate'),
		"todos": request.session.get('todos'),
		"notes": request.session.get('notes'),
		"bookmarks": request.session.get('bookmarks'),
		"search": request.session.get('search'),
		"toggle_viewtype": request.session.get('toggle_viewtype'),
		"tags": tags,
		"tag_quantities": tag_quantities
	}

	site = "index.html" if request.session.get('toggle_viewtype') == 'false' else "index-table.html"
	return render(request, site, context)

def get_db_as_json(request):
	todos = Todo.objects.all().values()
	notes = Note.objects.all().values()
	bookmarks = Bookmark.objects.all().values()
	# tags = Tag.objects.all()
	data = {
		'todos': list(todos),
		'notes' : list(notes),
		'bookmarks' : list(bookmarks)
	}
	return JsonResponse(data, safe=False)