import requests
import json
from datetime import date
import time
import smtplib, ssl

#Specify required state ID
url_district = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/141'
headers = {'accept': 'application/json','Accept-Language' : 'hi_IN','User-Agent': 'Mozilla/4.0'}
result = requests.get(url_district, headers=headers)
#print districts Ids
print(result.content.decode())
