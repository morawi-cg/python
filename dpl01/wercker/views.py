from django.shortcuts import render
from .forms import WerckerForm
from django.http import HttpResponse
from .models import WerckerModels
from json2html import *
import requests, json 

# Create your views here.
#def detail(request, question_id):
#class details(View):
#def detail(self,TokeName,Token):
#def detail(self):
def detail(request):
    werckerforms = WerckerForm(request.POST or None)

    if request.method == 'POST':
       if werckerforms.is_valid():
           werckerforms.save()
       
           url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
           headers = {'Authorization':'TokenName Token'}
           r = requests.get(url, headers=headers, verify=True)
           inp = r.json()
           ScreenValues = json2html.convert(json = inp)
           werckermodels = WerckerModels()
           werckermodels.TokenName = request.POST['TokeName']
           werckermodels.Token = request.POST['Token']
           #werckerforms = WerckerForm(request.POST)

           #ScreenValues = HttpResponse(json2html.convert(json = inp))
           #return HttpResponse("wercker Account details are %s." % question_id)
           return HttpResponse("Wercker Account Details are %s." % ScreenValues)
           #return ScreenValues
       else:

           return HttpResponse('Error')
    context = {'form': werckerforms}
    return render(request, 'wercker_account.html', context)


