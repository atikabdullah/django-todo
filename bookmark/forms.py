from django import forms

from .models import Bookmark


class BookmarkForm(forms.ModelForm):
	class Meta:
		model = Bookmark
		fields = ['name', 'description', 'url']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'description': forms.Textarea(attrs={'class': 'form-control mb-2 w-100'}),
			# 'tags': forms.CharField(attrs={'class': 'form-control mb-2 w-100'}),
			'url': forms.TextInput(attrs={'class': 'form-control mb-2', 'type': 'url'}),
		}
