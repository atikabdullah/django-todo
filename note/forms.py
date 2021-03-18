from django import forms

from .models import Note, Tag


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['name', 'tags', 'images', 'description', 'text_content']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'tags': forms.CheckboxSelectMultiple(choices=Tag.objects.all(), attrs={'class': 'form-control mb-2 w-100'}),
			# 'images':  forms.ImageField(label = 'Select a file', help_text= 'Jpg, jpeg only', required=False),
			'description': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'text_content': forms.Textarea(attrs={'class': 'form-control mb-2 w-100'}),
		}
