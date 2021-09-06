from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .views import *
urlpatterns = [
  path('',home,name='home'),
  path('blog/<slug:url>',post,name='post'),
  path('category/<slug:url>',category),
  path('blog/',blog,name='blog'),
  path('contact/',contact,name='contact'),
  path('about/',about,name='about')
]
