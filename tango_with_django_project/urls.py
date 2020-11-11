"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # 1. añadimos este url aquí y también en el file 'urls.py' en el directorio de la app 'rango', osea hacemos el mapping
    url(r'^$', views.index, name='index'), # 'index' es el nombre (name) que le ponemos a nuestro mapping xq es más facil referenciar al nombre que al urls

    #url(r'^$', views.about, name='about'), # creo que esta también está bien pero la de abajo tiene más sentido
    url(r'^rango/about/', views.about, name='about'),

    # 2. the following maps any URLs starting with rango/ to be handled by the rango app
    # Cuando voy a http://127.0.0.1:8000/rango/ me debe salir el return de la función 'index' de mis views, osea 'Rango says hey there partner!'
    url(r'^rango/', include('rango.urls')),

    url(r'^rango/about/', include('rango.urls')),

    url(r'^admin/', admin.site.urls),
    #path('admin/', admin.site.urls), este venía ya incluido


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
