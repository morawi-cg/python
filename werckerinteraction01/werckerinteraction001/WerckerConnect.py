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


ConnectToWercker_instance = WerckerConect(dpllogger,8348846cc6543d045b7e8030810a2e19074bba1b4a87a8d85f52316eaade3bd9)
ConnectToWercker_instance() #this is calling the __call__ method

