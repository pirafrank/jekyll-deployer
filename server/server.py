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
    return "The webhook server is running!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return show_html()

    if request.method != 'POST': # reject anything which is not get or post
        abort(501) # returns not implemented

    data = request.get_json()

    if not data['action'] == 'deploy':
        abort(501) # returns not implemented

    if data['deploy_type'] == 'stable':
        tasks.deploy(config,'stable')
        message = '**'+config['stable_branch']+'** branch has been deployed. \
View it at: '+config['stable_site_url']
        notify.tell_pushbullet(config,message)
        print message
        return 'OK'
    elif data['deploy_type'] == 'testing':
        tasks.deploy(config,'testing')
        message = '**'+config['testing_branch']+'** branch has been deployed. \
with drafts and future posts. You can access it from '+config['testing_site_url']
        notify.tell_pushbullet(config,message)
        print message
        return 'OK'
    else:
        message = "Error: unknown 'deploy_type' in json POST"
        notify.tell_pushbullet(config,message)
        print message
        return 'Error'

def main():
    default()
    app.run(host=config['host'], port=config['port'], debug=config['debug'])

if __name__ == '__main__':
    main()
