from django.contrib import admin
from news.models import News

# from filename.model import class nameof model
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=('title','descriptions')

admin.site.register(News, NewsAdmin)
