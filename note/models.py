from django.db import models
from django.utils import timezone


class Note(models.Model):
	name = models.CharField(max_length=50, null=False)
	card_description = models.CharField(max_length=120, null=True)
	description = models.TextField(max_length=8000, null=True)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
