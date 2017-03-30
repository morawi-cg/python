from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

# Patterns use was deprecated and the urlpaterns are equal to a list

urlpatterns = [

   url(r'^admin', include(admin.site.urls)),
   url(r'^wercker/', include('wercker.urls')),
]
