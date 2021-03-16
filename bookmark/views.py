from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import BookmarkForm
from .models import Bookmark



def bookmark_list(request):
	bookmarks = Bookmark.objects.all()
	paginator = Paginator(bookmarks, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		"page_obj": page_obj,

	}
	return render(request, "bookmark/bookmark_list.html", context)




def bookmark_detail(request, id):
	bookmark = Bookmark.objects.get(id=id)
	context = {
		"bookmark": bookmark,
	}
	return render(request, "bookmark/bookmark_detail.html", context)


def bookmark_create(request):
	form = BookmarkForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		form.save()
		return redirect('/bookmark/')
	return render(request, "Bookmark/bookmark_create.html", context)


def bookmark_update(request, id):
	bookmark = Bookmark.objects.get(id=id)
	form = BookmarkForm(request.POST or None, instance=bookmark)
	if form.is_valid():
		form.save()
		return redirect('/bookmark/')
	context = {
		"form": form,
	}
	return render(request, "bookmark/bookmark_update.html", context)


def bookmark_delete(request, id):
	bookmark = Bookmark.objects.get(id=id)
	bookmark.delete()
	return redirect('/bookmark/')

def bookmark_archive(request, id):
	bookmark = Bookmark.objects.get(id=id)
	if (bookmark.checked):
		bookmark.checked = False
		bookmark.save()
	else:
		bookmark.checked = True
		bookmark.save()
	return redirect('/bookmark/')
