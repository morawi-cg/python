#!/usr/bin/python3
import os, sys
# import authFile
from django.contrib import messages
import requests
import json
from json2html import *
os.system("../../../Auth/authFile.py")

class ConnectToWercker:
    def classcaller(self,TokenName,Token):
        self.TokenName = TokenName
        Self.Token = Token
        url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
        headers = {'Authorization':'TokenName Token'}
        r = requests.get(url, headers=headers, verify=True)

        inp = r.json()
        print(json2html.convert(json = inp))

## Now instansiate the class

ConnectToWercker_instance = ConnectToWercker() # ('dpllogger','8348846cc6543d045b7e8030810a2e19074bba1b4a87a8d85f52316eaade3bd9')
# ConnectToWercker_instance() #this is calling the __call__ method
ConnectToWercker_instance.classcaller('dpllogger','8348846cc6543d045b7e8030810a2e19074bba1b4a87a8d85f52316eaade3bd9')
