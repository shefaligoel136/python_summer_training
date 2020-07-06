"""student URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	path('', views.student,name="student"),
	path('slogin', views.slogin,name="slogin"),
	path('shome', views.shome,name="shome"),
	path('slogout', views.slogout,name="slogout"),
]
