#! python2

# jekyll-deployer client for Pythonista app
# github.com/pirafrank/jekyll-deployer
#
# Usage: Send this script to Pythonista on your iDevices,
# customize it, add it to your home screen, enjoy!
# Git branching model based on the famous post:
# http://nvie.com/posts/a-successful-git-branching-model/
#
# Assume that:
# - for all branches (but master) you want to deploy
# also drafts and future posts;
# - 'develop' is your integration branch. You can change
# it's name below.
#
# @Author
# Francesco Pira <dev at fpira dot com>
# fpira.com

import console
import dialogs
import urllib2
import json
import requests

# default settings, overwritten if choosen branch is master
is_production = False

# user prompt
branch = console.alert('Deployer','What do you want to deploy?','master','develop','Other branch...')

if branch == 1:
  is_production = True
elif branch == 2:
  branch = 'develop' # change this to your integration branch
elif branch == 3:
  branch = dialogs.text_dialog(title='Insert exact branch name:')
  branch = branch.split('\n')[0]
  # todo: add confirmation: you really want to deploy (branch name) to testing dir?
else:
  exit()

console.hud_alert('deploying '+branch+'...')

# data and configuration
api_token: "" # not implemented yet
config = {
    "action": "deploy",
    "deploy_branch": branch,
    "is_production": is_production
}

def post_request(token,payload):
    url = "https://fpira.com/webhooks/aaabbb111222333"
    headers = {"Access-Token":token,"Content-Type":"application/json"}
    data = payload

    r = requests.post(url, data=json.dumps(data), headers=headers)

if __name__ == '__main__':
    post_request(api_token,config)

