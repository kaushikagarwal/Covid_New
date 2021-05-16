import requests
import json
from datetime import date
import time
import smtplib, ssl

#API URL
url = 'http://cdn-api.co-vin.in/api/v2/admin/location/states'
headers = {'accept': 'application/json','Accept-Language' : 'hi_IN','User-Agent': 'Mozilla/4.0'}
result = requests.get(url, headers=headers)
#Print state ID
print(result.content.decode())
