from django.db import models
from django.utils import timezone


class Tag(models.Model):
	name = models.CharField(max_length=28)

	def __str__(self):
		return self.name


class Note(models.Model):
	name = models.CharField(max_length=50, null=False)
	tags = models.ManyToManyField(Tag, null=True)
	description = models.CharField(max_length=120, null=True)
	text_content = models.TextField(max_length=8000, null=True)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
