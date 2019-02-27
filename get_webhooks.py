import requests
import json
import yaml

url = 'https://api.ciscospark.com/v1/webhooks'

token = open("creds.yaml", "r")
headers = {"Authorization": "Bearer %s" % yaml.load(token)[3] }

response = requests.get(url, headers=headers)
rooms = json.loads(response.text)['items']

i = 0
while i < len(rooms):
    print rooms[i]['name'] 
    print rooms[i]
    i += 1

