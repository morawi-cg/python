from django.conf.urls import url, include
from tastypie.api import Api
from wercker.api import WerckerResource
api = Api(api_name='v1')
api.register(WerckerResource())
urlpatterns = [
url(r'api/', include(api.urls)),
]
