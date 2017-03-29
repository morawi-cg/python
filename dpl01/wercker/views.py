from django.shortcuts import render
from .models import WerckerModels
from json2html import *
import requests, json 

# Create your views here.
#def detail(request, question_id):
def detail(TokeName,Token):
    url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
    headers = {'Authorization':'TokenName Token'}
    r = requests.get(url, headers=headers, verify=True)
    inp = r.json()
          ScreenValues = json2html.convert(json = inp)
          ScreenValues = HttpResponse(json2html.convert(json = inp))
    #return HttpResponse("wercker Account details are %s." % question_id)

    return HttpResponse("Wercker Account Details are %s." % ScreenValues)

