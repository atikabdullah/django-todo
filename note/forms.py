from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['name', 'card_description','description']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'card_description': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'description': forms.Textarea(attrs={'class': 'form-control mb-2 w-100'}),
		}
