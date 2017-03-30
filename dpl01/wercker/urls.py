from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^detail/', 'wercker.views.detail', name = 'detail'),
     url(r'^$', views.detail, name='detail'),
]
