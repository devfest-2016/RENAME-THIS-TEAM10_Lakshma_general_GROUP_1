from httplib2 import Http
#from urllib import urlencode
#import pprint
#
#pp = pprint.PrettyPrinter(indent=4)
#def printer(stuff):
#    return pp.pprint(stuff)
#
#
#url = 'http://script.google.com/macros/s/AKfycbxMsw8uypjUeuBV8-75YiMlonNJIZQl-tkPe0BT6uIUIMhm3tCV/exec'
#
#random = 'url=image.com&status=infected&coordinates=1.1.2&treatment=fumigate&result=cured'
#
#content = {
#    'url': 'image.com',
#    'status': 'infected',
#    'coordinates': '1.1.1',
#    'treatment': 'fumigate',
#    'result': 'cured'
#    }
#
#request_object = urllib.request.Request(url, data=random)
#printer(urllib.request.urlopen(request_object))

#h = Http()
data = dict(url="image.com", status="infected", coordinates="1.1.1", treatment="fumigate", result="cured")

url = 'http://script.google.com/macros/s/AKfycbxMsw8uypjUeuBV8-75YiMlonNJIZQl-tkPe0BT6uIUIMhm3tCV/exec'
#resp, content = h.request(url, "POST", urlencode(data))

#print(resp)

import requests
payload = {'url': 'image.com', 'status': 'infected', 'coordinates': '1.1.1', 'treatment': 'fumigate', 'result': 'cured'}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON 
import json
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
print(r.text)
print(r.status_code)
