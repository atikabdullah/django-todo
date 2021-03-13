from django.db import models


class Todo(models.Model):
	name = models.CharField(max_length=90)
	description = models.CharField(max_length=500)
	due_date = models.DateField()
	checked = models.BooleanField(default=False)

	def __str__(self):
		return self.name
