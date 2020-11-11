from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # el mapping de este url está en 'urls.py' en el directorio principal tango_with_django_project
    url(r'^about/', views.about, name='about'),
]