from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from wercker.models import wercker
 
 
class WerckerResource(ModelResource):
#“””Resource for wercker
#“””
 class Meta:
   queryset = wercker.objects.all()
   resource_name = 'wercker'
   authorization = Authorization() # This poses a risk factor, its flexibility at cost only enable within a strickt environment!
   filtering = { 
   

   }


