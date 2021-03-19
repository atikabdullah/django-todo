from django.db import models
from django.utils import timezone

from tags.models import Tag


class ArticleImage(models.Model):
	image = models.FileField(upload_to='uploads/%Y/%m/%d/')

	def __str__(self):
		return self.image.name


class Note(models.Model):
	name = models.CharField(max_length=50, null=False)
	tags = models.ManyToManyField(Tag, related_name='note_tags')
	images = models.ForeignKey(ArticleImage, null=True, on_delete=models.CASCADE)
	description = models.CharField(max_length=120, null=True)
	text_content = models.TextField(max_length=8000, null=True)
	item_type = models.CharField(default="Note", max_length=16, null=False)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
