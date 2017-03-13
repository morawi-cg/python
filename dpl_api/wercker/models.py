from django.db import migrations, models
import os, sys
import requests
import json
from json2html import *

#os.system("../../../../../Auth/authFile.py")
url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
headers = {'Authorization':'TokenName Token'}

class Wercker(models.Model):

    TokenName = models.CharField(max_length=30,help_text="name of the wercker token")
    Token = models.CharField(max_length=30,help_text="This is the wercker token")
    #url = models.CharField(default=None,max_length=255,help_text="BuildTool API url")
    r = requests.get(url, headers=headers, verify=True)
    inp = r.json()
    print(json2html.convert(json = inp))
    def _unicode_(self):
         return self.choice_text
