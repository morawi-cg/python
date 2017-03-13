from tastypie.resources import ModelResource
from wercker.models import Wercker,
 
 
class WerckerResource(ModelResource):
“””Resource for Wercker
“””
class Meta:
queryset = Wercker.objects.all()
resource_name = ‘wercker’
