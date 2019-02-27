import requests
import json
import yaml

url = 'https://api.ciscospark.com/v1/rooms'

token = open("creds.yaml", "r")
headers = {"Authorization": "Bearer %s" % yaml.load(token) }

response = requests.get(url, headers=headers)
rooms = json.loads(response.text)['items']

i = 0
while i < len(rooms):
    print rooms[i]['title'] 
    i += 1

