from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Service_Member(models.Model):
    service_title  = models.CharField(max_length=500)
    service_desc = HTMLField()
    service_slug = AutoSlugField(
        populate_from='service_title', unique=True, null=True, default=None)
    service_pdf = models.FileField(
        upload_to="service/", max_length=250, null=True, default=None)

 
