from django.conf.urls import url


from . import views as usuarios

#...otros imports...


urlpatterns = [
	url(r'^configuracion/$', usuarios.conf_cuenta, name='conf_cuenta' ),
	url(r'^configuracion/perfil$', usuarios.conf_perfil, name='conf_perfil' ),
	url(r'^configuracion/password$', usuarios.conf_pass, name='conf_pass' ),
	url(r'^ayuda/$', usuarios.ayuda, name='ayuda' ),
]