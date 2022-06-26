"""Jardineria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django import urls
from django.contrib import admin
from django.urls import path, include
from Jardineria.settings import DEBUG
from core.views import home, formularioContacto, Donativos, metodoPago, registrar, contacto
from django.conf import settings
from django.conf.urls.static import static


from core.views import Donativos, home, metodoPago, registrar, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('home/', home),
    path('formularioContacto/', formularioContacto),
    path('Donativos/', Donativos),
    path('metodoPago/', metodoPago),
    path('registrar/', registrar),
    path('contacto/', contacto)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

