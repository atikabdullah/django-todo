from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['name', 'description', 'checked', 'due_date']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-2 w-100'}),
			'description': forms.Textarea(attrs={'class': 'form-control mb-2 w-100'}),
			'checked': forms.CheckboxInput(attrs={'class': 'form-control mb-2 w-100'}),
			'due_date': forms.TextInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
		}
