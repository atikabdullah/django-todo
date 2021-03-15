from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Todo(models.Model):
	name = models.CharField(max_length=90)
	description = models.CharField(max_length=500)
	due_date = models.DateField()
	checked = models.BooleanField(default=False)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
