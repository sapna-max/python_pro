from django.db import models
from datetime import datetime

# Create your models here.
class saveregistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    appodate = models.DateTimeField(default=datetime.now)