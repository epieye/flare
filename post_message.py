import requests
import json
import yaml

url = 'https://api.ciscospark.com/v1/messages'

token = open("creds.yaml", "r")
headers = {"Authorization": "Bearer %s" % yaml.load(token)[1] }
data = {"toPersonEmail": "warren.matthews@here.com", "markdown": "Test python client."} 

response = requests.post(url, headers=headers, data=data)

#print response.text
