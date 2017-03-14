from tastypie.resources import ModelResource
from wercker.models import wercker
 
 
class WerckerResource(ModelResource):
#“””Resource for wercker
#“””
 class Meta:
   queryset = wercker.objects.all()
   resource_name = 'wercker'
