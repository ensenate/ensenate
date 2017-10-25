from django.conf.urls import url, include

from . import views

from django.contrib.auth.views import login

urlpatterns = [
# Examples:
# url(r'^$', 'ensenate.views.home', name='home'),
	url(r'^login/$', login, { 'template_name': 'principal/login.html' }, name='login'),

	url(r'^$', views.principal, name='principal'),

	#social-auth
	url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
	
]