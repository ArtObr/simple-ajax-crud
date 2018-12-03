from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.bank import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^account/$', views.account_list, name='account_list'),
    url(r'^account/create/$', views.account_create, name='account_create'),
    url(r'^account/(?P<pk>\d+)/update/$', views.account_update, name='account_update'),
    url(r'^account/(?P<pk>\d+)/delete/$', views.account_delete, name='account_delete'),
]
