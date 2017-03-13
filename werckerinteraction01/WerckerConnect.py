import os, sys
import requests
import json
from json2html import *
os.system("../../../../Auth/authFile.py")
url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
headers = {'Authorization':'TokenName Token'}



class WerckerConect:
    def __init__(self,TokenName,Token):

        r = requests.get(url, headers=headers, verify=True)
        inp = r.json()
        print(json2html.convert(json = inp))


#ConnectToWercker_instance = ConnectToWercker()
#ConnectToWercker_instance() #this is calling the __call__ method

