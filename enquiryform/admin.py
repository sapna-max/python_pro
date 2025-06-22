from django.contrib import admin
from enquiryform.models import saveenquiry

# Register your models here.

class contactEnquiry(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')

admin.site.register(saveenquiry, contactEnquiry)