from django.contrib import admin

from .models import Note, Tag, ArticleImage

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(ArticleImage)
