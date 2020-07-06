"""student URL Configuration"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.student,name='student'),
    path('slogin',views.slogin,name='slogin'),
    path('shome',views.shome,name='shome'),
    path('slogout',views.slogout,name='slogout'),
    path('s_chk_marks',views.s_chk_marks,name='s_chk_marks'),
]
