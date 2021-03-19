from itertools import chain

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from queryset_sequence import QuerySetSequence
from bookmark.models import Bookmark
from crashcourse.forms import CustomUserCreationForm
from note.models import Note
from todo.models import Todo

class SignupView(generic.CreateView):
	template_name = "registration/signup.html"
	form_class = CustomUserCreationForm

	def get_success_url(self):
		return reverse("login")


def set_session(request):
	for var in ['todos', 'notes', 'bookmarks', 'sortbycreation']:
		request.session[var] = 'true'
	for var in ['sortbytype', 'sortbyduedate', 'toggle_viewtype', 'no_item_filtering_allowed']:
		request.session[var] = 'false'
	for var in ['search', 'active_tag']:
		request.session[var] = ''
	request.session['session_initialized'] = 'true'
	enable_item_filtering(request)
	return request


def disable_item_filtering(request):
	for var in ['todos', 'notes', 'bookmarks', 'no_item_filtering_allowed']:
		request.session[var] = 'true'


def enable_item_filtering(request):
	request.session['no_item_filtering_allowed'] = 'false'


def update_session(request):
	if request.session['no_item_filtering_allowed'] == 'true':
		pass
	elif request.POST.get('todos') or request.POST.get('notes') or request.POST.get('bookmarks'):
		for item_type in ['todos', 'notes', 'bookmarks']:
			request.session[item_type] = request.POST.get(item_type)
	if request.POST.get('sortbycreation') or request.POST.get('toggle_viewtype'):
		request.session['toggle_viewtype'] = request.POST.get('toggle_viewtype')
		if request.POST.get('sortbycreation') == 'true':
			request.session['sortbycreation'] = request.POST.get('sortbycreation')
	if request.POST.get('search') and request.POST.get('reset') != 'true':
		request.session['search'] = request.POST.get('search')
	elif request.POST.get('search') and request.POST.get('reset') == 'true':
		request.session['search'] = ''
	if request.POST.get("cleartags") == 'true':
		request.session['active_tag'] = ''
		enable_item_filtering(request)
	return request


def list_all(request):
	if request.session.get('session_initialized') != 'true':
		request = set_session(request)
		redirect('/')

	if request.POST:
		request = update_session(request)
		if request.POST.get("cleartags") == 'true':
			return HttpResponseRedirect(redirect_to='/')
		redirect('/')
	queryset = list()
	todos = Todo.objects.all() if request.session.get('todos') == 'true' else None
	notes = Note.objects.all() if request.session.get('notes') == 'true' else None
	bookmarks = Bookmark.objects.all() if request.session.get('bookmarks') == 'true' else None
	tag_quantities = get_tags_count()

	if request.GET.get("tags"):
		disable_item_filtering(request)
		request.session['active_tag'] = request.GET.get("tags")
		if todos is not None:
			todos = todos.filter(tags__name__in=[request.GET.get("tags")])
		if notes is not None:
			notes = notes.filter(tags__name__in=[request.GET.get("tags")])
		if bookmarks is not None:
			bookmarks = bookmarks.filter(tags__name__in=[request.GET.get("tags")])

	for item in [todos, notes, bookmarks]:
		if item is not None:
			queryset.append(item)

	all_items = QuerySetSequence(*queryset). \
		order_by('-date_created' if request.session.get('sortbycreation') == 'true' else 'date_created'). \
		filter(Q(name__contains=request.session.get('search')) | Q(description__contains=request.session.get('search')))

	paginator = Paginator(all_items, 3)

	site = "index.html" if request.session.get('toggle_viewtype') == 'false' else "index-table.html"
	return render(request, site, context={
		"page_obj": paginator.get_page(request.GET.get('page')),
		"tag_quantities": tag_quantities,
		"active_tag": request.session['active_tag']})


def get_tags_count():
	""" Returns a list of tuples with tags and how many items are registered with each respective tag.
	[('Django', 3), ... ('Important', 8)] """
	tags_quantities_per_object = chain(
		Note.objects.values_list('tags__name').annotate(c=Count('tags__name')).order_by('-c'),
		Bookmark.objects.values_list('tags__name').annotate(c=Count('tags__name')).order_by('-c'),
		Todo.objects.values_list('tags__name').annotate(c=Count('tags__name')).order_by('-c'),
	)
	tag_quantities = dict()
	for name, val in list(tags_quantities_per_object):
		if tag_quantities.get(name) is not None:
			new_quantity = int(val) + int(tag_quantities.get(name))
			tag_quantities.update({name: new_quantity})
		else:
			tag_quantities.update({name: val})
	tag_quantities = tag_quantities.items()
	return tag_quantities


def get_db_as_json(request):
	data = {
		'todos': list(Todo.objects.select_related('tags__todo_tags').all().values()),
		'notes': list(Note.objects.select_related('tags__note_tags').all().values()),
		'bookmarks': list(Bookmark.objects.all().values())
	}
	return JsonResponse(data, safe=False)
