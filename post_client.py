# Several package for a REST client. Pick one.
# https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python

import requests
import json

url = 'http://192.168.1.36:5000/user/Bob'

new_user = { "name": "Bob", "age": "99", "occupation": "Carpenter" }

response = requests.post(url, data=new_user)
print response.text
