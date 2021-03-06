"""wangpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from web1 import views, admin
from web1.api import api

urlpatterns = [
    #  url(r'^admin/', admin.urls),
    url(r'^index', views.index),
    url(r'^test_get', views.test_get),
    url(r'^openstack_test', views.openstack_test),
    url(r'^vsphere_test', views.vsphere_test),
    url(r'^api_test', api.product_class.as_view()),
]
