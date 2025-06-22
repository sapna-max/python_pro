from django.contrib import admin
from service.models import Service_Member

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_desc', 'service_pdf')

admin.site.register(Service_Member, ServiceAdmin)

# Register your models here.
