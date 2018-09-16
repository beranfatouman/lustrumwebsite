from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index, name='index'),
	path('details/<int:id>/', views.details, name='index'),
	path('upvote/<int:id>/', views.upvote, name='index'),
	url(r'^(?P<pk>\d+)/meldaan/$', views.meld_u_aan, name='meld_u_aan'),
	#path('upvote/<int:id>/', views.upvote, name='upvote')
]




