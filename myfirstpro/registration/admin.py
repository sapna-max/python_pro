from django.contrib import admin
from registration.models import saveregistration

# Register your models here.
class contactEnquiry(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message','appodate')

admin.site.register(saveregistration, contactEnquiry)