from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from wercker.models import werckermodels
 
 
class WerckerResource(ModelResource):
#“””Resource for wercker
#“””
 class Meta:
   queryset = werckermodels.objects.all()
   resource_name = 'werckerModules'
   authorization = Authorization() # This poses a risk factor, its flexibility at cost only enable within a strickt environment!
   filtering = { 
   

   }


