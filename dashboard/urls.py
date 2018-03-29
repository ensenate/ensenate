from django.conf.urls import url


from . import views as dashboard

from django.conf import settings
#...otros imports...


urlpatterns = [
	url(r'^dashboard/$', dashboard.inicio, name='dashboard' ),

	url(r'^perfil/$', dashboard.perfil, name='perfil' ),
	
	url(r'^unidad/(?P<unidad>[^/]+)$', dashboard.detalle_unidad,
                           name='lecciones'),
	
	url(r'^vista/(?P<unidad>[^/]+)/(?P<leccion>\d+)$', dashboard.vista_previa,
                           name='vista_previa'),	
	url(r'^aprender/(?P<unidad>[^/]+)/(?P<leccion>\d+)$', dashboard.aprender,
                           name='aprender'),
	url(r'^confirmar/(?P<unidad>[^/]+)/(?P<leccion>\d+)$', dashboard.confirmar,
                           name='confirmar'),
]

if settings.DEBUG:
	urlpatterns += [
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 
		'document_root': settings.MEDIA_ROOT}), 
	]