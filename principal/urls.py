from django.conf.urls import url, include

from . import views

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
# Examples:
# url(r'^$', 'ensenate.views.home', name='home'),
	#login normal 
	url(r'^login/$', login, { 'template_name': 'principal/login.html' }, name='login'),
	#social-auth
	url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

	#logout sirve para ambos casos
	url(r'^logout/$', logout, { 'next_page': 'login' }, name='logout'),


 	#restablecer contraseña
	url(r'^restablecer_password/$', password_reset, { 'template_name' : 'principal/restaurar-password/password_reset_form.html', 'email_template_name' : 'principal/restaurar-password/password_reset_email.html' }, name='password_reset'),
	url(r'^restablecer_password/hecho/$', password_reset_done, { 'template_name' : 'principal/restaurar-password/password_reset_done.html' }, name='password_reset_done'),
	url(r'^nueva_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,  { 'template_name' : 'principal/restaurar-password/password_reset_confirm.html'}, name='password_reset_confirm'),
	url(r'^nueva_password/hecho/$', password_reset_complete, { 'template_name' : 'principal/restaurar-password/password_reset_complete.html'}, name='password_reset_complete'),


	#vista de inicio
	url(r'^$', views.inicio.as_view(), name='inicio'),

	#vista de registro
	url(r'^crear_usuario/$', views.registrar_usuario, name='registrar_usuario'),	



	
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
]