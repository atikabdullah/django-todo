from django.db import models
from django.utils import timezone

from tags.models import Tag


class Bookmark(models.Model):
	name = models.CharField(max_length=90)
	tags = models.ManyToManyField(Tag, related_name='bookmark_tags')
	description = models.CharField(max_length=500)
	url = models.URLField()
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
