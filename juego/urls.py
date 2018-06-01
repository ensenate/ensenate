# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views as juego

urlpatterns = [
# Examples:
# url(r'^$', 'ensenate.views.home', name='home'),
	url(r'^juego/(?P<nombre_juego>[^/]+)/$', juego.juego , name='juego'),
	url(r'^guardar/(?P<nombre_juego>[^/]+)/(?P<puntos>[^/]+)/$', juego.guardar , name='guardar'),
]