from django.conf.urls import url


from . import views as dashboard

from django.conf import settings
#...otros imports...


urlpatterns = [
	url(r'^dashboard/$', dashboard.inicio, name='dashboard' ),

	url(r'^perfil/$', dashboard.perfil, name='perfil' ),
	
	url(r'^leccion/(?P<pk>\d+)$', dashboard.lecciones,
                           name='lecciones'),
	
	url(r'^practica/(?P<unidad>[^/]+)/(?P<leccion>\d+)$', dashboard.practica,
                           name='practica'),
]

if settings.DEBUG:
	urlpatterns += [
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 
		'document_root': settings.MEDIA_ROOT}), 
	]