from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [
# Examples:
# url(r'^$', 'ensenate.views.home', name='home'),
	url(r'^$', login, { 'template_name' : 'principal/login.html' }, name='login'),
	
]