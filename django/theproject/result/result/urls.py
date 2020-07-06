"""result URL Configuration"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('faculty/',include('faculty.urls')),
    path('student/',include('student.urls')),
    path('admin/', admin.site.urls),
]
