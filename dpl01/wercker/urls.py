from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
    url(r'^detail/', 'wercker.views.detail', name = 'detail'),

]
