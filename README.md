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
- deploy any branch, options:
    - deploy production or testing branch in one tap
    - deploy any other branch by typing its name (`v2.0`)
- deploy to a testing location (e.g. `test.mywebsite.com`)
- deploy drafts and future posts to a testing location
- notifications to your smartphone/tablet

## Requirements

- A VPS with these installed:
    - Python 2.6+ but < 3.x
    - a reverse proxy server (nginx handles this awesomely)
    - jekyll (needed to actually generate the website)
    - rsync
- A Pushbullet account (cause everyone likes pocket notifications)
- your website has to stay in a git repo (of course...)

## Versions

- `2.0`: break changes: POST parameters are different from `v1.0`
- `1.0`: first version

## License

The software in this repository are released under the GNU GPLv3 License by Francesco Pira (dev[at]fpira[dot]com, fpira.com). You can read the terms of the license [here](http://www.gnu.org/licenses/gpl-3.0.html).
