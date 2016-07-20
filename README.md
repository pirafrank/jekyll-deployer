# jekyll-deployer

That's what a developer on-the-go do when it's tired of ssh-ing to VPS to publish his blog posts :P

## Scenario

- you have a Jekyll website hosted on your VPS
- you write from any device (e.g. using an app like iA Writer) than commit and push to repo on-the-go

**jekyll-deployer** running on your VPS will:

1. `pull` changes from your jekyll website repo
2. generated the website and deploy it
3. Send you a notification on your phone/tablet

## Features

- one-touch deploy to production (stable) or testing environment
- post scheduling
- deploy to a testing location (e.g. test.mywebsite.com)
- deploy drafts and future posts to a testing location
- notifications to your smartphone/tablet

## Requirements

- A VPS with these installed:
    - Python 2.6+ but < 3.x
    - a reverse proxy server (nginx handles this awesomely)
    - jekyll (needed to actually generate the website)
    - rsync
- [BitBucket.org](http://bitbucket.org) as git server
- A Pushbullet account (cause everyone likes pocket notifications)
- your website has to stay in a git repo (of course...)

## More info soon!
