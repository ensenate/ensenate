from django.conf.urls import url, include

from . import views

from django.contrib.auth.views import login, logout

urlpatterns = [
# Examples:
# url(r'^$', 'ensenate.views.home', name='home'),
	url(r'^login/$', login, { 'template_name': 'principal/login.html' }, name='login'),

	url(r'^logout/$', logout, { 'next_page': 'login' }, name='logout'),

	url(r'^$', views.inicio, name='inicio'),

	url(r'^dashboard/$', views.dashboard, name='dashboard'),

	#url(r'^logout/$', views.logout, name='logout'),	

	#social-auth
	url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
	
]