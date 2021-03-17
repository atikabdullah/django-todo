from django.shortcuts import render, redirect

from .forms import NoteForm
from .models import Note


#
# def note_list(request):
# 	notes = Note.objects.all()
# 	paginator = Paginator(notes, 12)
# 	page_number = request.GET.get('page')
# 	page_obj = paginator.get_page(page_number)
# 	context = {
# 		"page_obj": page_obj,
#
# 	}
# 	return render(request, "note/note_list.html", context)


def note_detail(request, id):
	note = Note.objects.get(id=id)
	context = {
		"note": note,
	}
	return render(request, "note/note_detail.html", context)


def note_create(request):
	form = NoteForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		form.save()
		return redirect('/note/')
	return render(request, "note/note_create.html", context)


def note_update(request, id):
	note = Note.objects.get(id=id)
	form = NoteForm(request.POST or None, instance=note)
	if form.is_valid():
		form.save()
		return redirect('/')
	context = {
		"form": form,
	}
	return render(request, "note/note_update.html", context)


def note_delete(request, id):
	note = Note.objects.get(id=id)
	note.delete()
	return redirect('/note/')


def note_archive(request, id):
	note = Note.objects.get(id=id)
	if (note.checked):
		note.checked = False
		note.save()
	else:
		note.checked = True
		note.save()
	return redirect('/note/')
