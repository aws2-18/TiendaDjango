"""djangodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from productes.views import ProducteListView
#from productes.views import mostra_carrito
from productes.views import MostraCarritoView
from productes.views import afegeix
from productes.views import tancar
from productes.views import producte
from productes.views import carrito
from productes.views import abrir
#from django import oldforms as forms


urlpatterns = [
    url(r'^$', ProducteListView.as_view() ),
    url(r'^admin/', admin.site.urls),
    url(r'^carritos', MostraCarritoView.as_view() ),
    url(r'^afegeix/(?P<producte_id>[0-9]+)', afegeix ),
    url(r'^tancar', tancar),
    url(r'^producte/(?P<id>[0-9]+)$', producte),
    url(r'^carrito/(?P<id>[0-9]+)$', carrito),
    url(r'^abrir/(?P<id>[0-9]+)$', abrir)
]

