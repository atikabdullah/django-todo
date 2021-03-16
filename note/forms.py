from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['name', 'tags','description','text_content']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'tags': forms.CheckboxInput(attrs={'class': 'form-control mb-2 w-100'}),
			'description': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'text_content': forms.Textarea(attrs={'class': 'form-control mb-2 w-100'}),
		}
