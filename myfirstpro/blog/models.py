from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_desc = HTMLField()
    blog_slug = AutoSlugField(
        populate_from='blog_title', unique=True, null=True, default=None)
    blog_image = models.FileField(
        upload_to="blog/", max_length=250, null=True, default=None)