import jwt
#encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

#print(jwt.decode(encoded, 'secret', algorithms=['HS256']))

import requests

myToken = 'ABCD'  #(Dummy token, have copied actual token from session storage in chrome)
myUrl ="https://api.github.com"

head = {'Authorization': 'Bearer {}'.format(myToken)}
headers = {'content-type': 'application/json'}

response = requests.get(url = myUrl)

pastebin_url = response.text 

print(pastebin_url)