from django.db import models


# class Tag(models.Model):
# 	CHOICES = {
# 		("Programming", "Programming"),
# 		("Tutorial", "Tutorial"),
# 		("Video", "Video"),
# 	}
# 	tag = models.CharField(choices=CHOICES, max_length=30)
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Bookmark(models.Model):
	name = models.CharField(max_length=90)
	description = models.CharField(max_length=500)
	# tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
	url = models.URLField()
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
