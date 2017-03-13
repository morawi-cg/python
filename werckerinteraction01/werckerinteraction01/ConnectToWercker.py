#!/usr/bin/python3
import os, sys
# import authFile
import requests
import json
from json2html import *
os.system("../../../../Auth/authFile.py")
url = 'https://app.wercker.com/api/v3/applications/wercker/docs'
#url = 'https://app.wercker.com/api/v3/'
headers = {'Authorization':'TokenName Token'}
r = requests.get(url, headers=headers, verify=True)
#print (r.json())

outp = {}
inp = r.json()
print(json2html.convert(json = inp))


