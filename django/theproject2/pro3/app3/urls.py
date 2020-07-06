from django.urls import path
from . import views
urlpatterns = [
	path('', views.home,name="home"),
	path('solve1', views.solve1,name="solve1"),
	path('solve2', views.solve2,name="solve2"),
]
                                    