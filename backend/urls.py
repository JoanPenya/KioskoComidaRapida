"""burgerbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from burger import views
from burger.views import *
from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/customers/$', views.customers_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
    url(r'^api/product/$', views.product_list),
    url(r'^api/product/(?P<pk>[0-9]+)$', views.product_detail),
    url(r'^api/product/Hamburguesa/$', views.product_hamburguesa),
    url(r'^api/product/Menu/$', views.product_menu),
    url(r'^api/product/Bebidas/$', views.product_bebidas),
    url(r'^api/product/Complementos/$', views.product_complementos),
    url(r'^api/product/Otros/$', views.product_otros),
    url(r'^api/product/Postre/$', views.product_postre),
    url(r'^api/product/Ofertas/$', views.product_ofertas),
    url(r'^api/cxp/$', views.CxP_list),
    url(r'^api/cxp/(?P<pk>[0-9]+)$', views.CxP_detail),
]