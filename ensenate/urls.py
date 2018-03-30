from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	# Examples:
	# url(r'^$', 'ensenate.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'favicon.ico')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('principal.urls')),
	url(r'', include('dashboard.urls')),
	url(r'', include('usuarios.urls')),
]
