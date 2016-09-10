import os
import json
from flask import Flask, request, abort
import notify
import tasks

#
# global vars
#

app = Flask(__name__)
path = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))

# load config
with open(os.path.join(path, 'config.json'), 'r') as conf:
    config = json.loads(conf.read())

#
# functions
#

def default():
    print 'Webhook server online on host: '+config['host']+', port:',config['port']

def show_html():
    return "The webhook server is running! There's no much to do here."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_html()

    if request.method != 'POST': # reject anything which is not get or post
        abort(501) # returns not implemented

    data = request.get_json()

    if not data['action'] == 'deploy':
        message = "Error: unknown action in POST. Deploy aborted."
        notify.tell_pushbullet(config,message)
        abort(501) # returns not implemented

    if data['is_production'] == True: # deploying master to production dir
        tasks.deploy(config['repository_dir'],config['stable_branch'],config['stable_deploy_dir'],config['stable_deploy_command'])
        tasks.postrun(config['postrun_command'])
        message = '**'+config['stable_branch']+'** branch has been deployed. \
You can access it from: '+config['stable_site_url']
        notify.tell_pushbullet(config,message)
        print message
        return 'OK'
    elif data['is_production'] == False: # deploying other branches to testing dir
        tasks.deploy(config['repository_dir'],data['deploy_branch'],config['testing_deploy_dir'],config['testing_deploy_command'])
        message = '**'+data['deploy_branch']+'** branch has been deployed \
with drafts and future posts. You can access it from '+config['testing_site_url']
        notify.tell_pushbullet(config,message)
        print message
        return 'OK'
    else:
        message = "Error: unknown value for is_production variable in json POST"
        notify.tell_pushbullet(config,message)
        print message
        return 'Error'

def main():
    default()
    app.run(host=config['host'], port=config['port'], debug=config['debug'])

if __name__ == '__main__':
    main()
