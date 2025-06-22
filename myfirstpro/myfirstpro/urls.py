"""
URL configuration for myfirstpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfirstpro import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


handler404='myfirstpro.views.error_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('blog-single', views.blog),
    path('homepage', views.homePage),
    path('contact', views.contact),
    path('service/', views.service),
    path('aboutus', views.aboutUs),
    path('error', views.error),
    path('blogdata', views.blogdata),
    path('Course-details/<int:courseid>', views.CourseDetails),
    path('Course-string/<str:coursestr>', views.Coursestring),
    path('Course-slug/<slug:courseslug>', views.Courseslugdata),
    path('data', views.current_datetime),
    path('contactEnquiry', views.contactEnquiry, name="contactEnquiry"),
    path('savereg', views.savereg, name="savereg"),
    path('registration', views.registration),
    path('servicedetails/<slug>', views.servicedetails),
    path('email_multi_alternatives/', views.email_multi_alternatives),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)