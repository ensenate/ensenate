from django.conf.urls import url


from . import views as dashboard

urlpatterns = [
	url(r'^dashboard/$', dashboard.inicio, name='dashboard' ),
]