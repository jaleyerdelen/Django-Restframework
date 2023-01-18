from django.contrib import admin
from news.models import Article, Journalist

# Register your models here.
admin.site.register(Article)
admin.site.register(Journalist)