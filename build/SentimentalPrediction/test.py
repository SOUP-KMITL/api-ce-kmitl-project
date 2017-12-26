import json
import requests
from pprint import pprint
from config import socialDataService

key = "8d8f1218-c640-4189-a0cd-6d69043b0795"#"f9a5e9e2-1287-4b51-872c-76a8df41bcc8"
geolocation = requests.get('http://'+socialDataService+'/place', {'place_id': key}).json()#['place']['geolocation']
print (type(geolocation))
pprint(geolocation)
