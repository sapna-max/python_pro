from django.db import models

# Create your models here.
class saveenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    