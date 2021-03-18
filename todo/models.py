from django.db import models
from django.utils import timezone

# class Tag(models.Model):
# 	name = models.CharField(max_length=28)
#
# 	def __str__(self):
# 		return self.name
from tags.models import Tag


class Todo(models.Model):
	name = models.CharField(max_length=90)
	tags = models.ManyToManyField(Tag, related_name='todo_tags')
	description = models.CharField(max_length=500)
	due_date = models.DateField()
	checked = models.BooleanField(default=False)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
