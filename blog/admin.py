from django.contrib import admin
from django.contrib.admin.sites import site
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_desc', 'blog_image')


admin.site.register(Blog, BlogAdmin)

# Register your models here.
