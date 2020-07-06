"""Faculty URL Configuration"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.faculty,name="faculty"),
	path('flogin', views.flogin,name="flogin"),
	path('fhome', views.fhome,name="fhome"),
	path('flogout', views.flogout,name="flogout"),
	path('faccount', views.faccount,name="faccount"),
	path('create_account', views.create_account,name="create_account"),
	path('marks', views.marks,name="marks"),
	path('update_marks', views.update_marks,name="update_marks"),
	
]
