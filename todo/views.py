from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


def todo_list(request):
	todos = Todo.objects.all().order_by('due_date')
	paginator = Paginator(todos, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		"page_obj": page_obj,

	}
	return render(request, "todo/todo_list.html", context)


def todo_detail(request, id):
	todo = Todo.objects.get(id=id)
	context = {
		"todo": todo,
	}
	return render(request, "todo/todo_detail.html", context)


def todo_create(request):
	form = TodoForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		form.save()
		return redirect('/todo/')
	return render(request, "todo/todo_create.html", context)


def todo_update(request, id):
	todo = Todo.objects.get(id=id)
	form = TodoForm(request.POST or None, instance=todo)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {
		"form": form,
	}
	return render(request, "todo/todo_update.html", context)


def todo_check(request, id):
	todo = Todo.objects.get(id=id)
	if (todo.checked):
		todo.checked = False
		todo.save()
	else:
		todo.checked = True
		todo.save()
	return redirect('/todo/')


def todo_delete(request, id):
	todo = Todo.objects.get(id=id)
	todo.delete()
	return redirect('/todo/')
