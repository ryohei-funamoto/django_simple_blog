from django.contrib import admin
from simple_blog.models import Article, Comment

# Register your models here.

admin.site.register([Article, Comment])
