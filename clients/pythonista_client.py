import console
import urllib2
import json
import requests

type = console.alert('Deployer','What do you want to deploy?','stable','testing')

if type == 1:
  type = 'stable'
elif type == 2:
  type = 'testing'
else:
  exit()

console.hud_alert('deploying '+type+'...')

config = {
    "api_token": "",
    "action": "deploy",
    "deploy_type": type
}

def post_request(config):
    url = "https://fpira.com/webhooks/aaabbb111222333"
    headers = {"Access-Token":config['api_token'],"Content-Type":"application/json"}
    data = {"action":config['action'],"deploy_type":config['deploy_type']}

    r = requests.post(url, data=json.dumps(data), headers=headers)

if __name__ == '__main__':
    post_request(config)

