import json
import requests

def tell_pushbullet(config,message):
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {"Access-Token":config['pushbullet_token'],"Content-Type":"application/json"}
    data = {"body":message,"title":config['service_name'],"type":"note"}

    r = requests.post(url, data=json.dumps(data), headers=headers)
