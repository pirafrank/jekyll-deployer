#!/bin/bash

#
# Variables
#

REPO_DIR="$1"
GIT_BRANCH="$2"
DEPLOY_DIR="$3"
DEPLOY_COMMAND="$4"

#
# Script
#

if [[ $# != 4 ]]; then
    echo "Error: wrong number of arguments"
    echo "Usage: ./deploy.sh [repo_dir] [git branch] [target path] [stable|testing]"
    exit 1
fi

# check if jekyll and rsync are installed
hash "jekyll" 2>/dev/null || { echo >&2 "jekyll is required but it's not installed. Aborting."; exit 1; }
hash "rsync" 2>/dev/null || { echo >&2 "rsync is required but it's not installed. Aborting."; exit 1; }
hash "git" 2>/dev/null || { echo >&2 "git is required but it's not installed. Aborting."; exit 1; }

if [ ! -d "$REPO_DIR" ]; then
    echo "Error: repo directory does not exists. Exiting..."
    exit 1
fi
cd $REPO_DIR

git remote update origin --prune
git checkout -f $GIT_BRANCH
sleep 1
echo "Current branch is: $(git branch | sed -n -e 's/^\* \(.*\)/\1/p')"
git reset --hard HEAD
git pull origin $GIT_BRANCH

if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Error: $DEPLOY_DIR doesn't exist. Please, check it and try again. Aborting..."
    exit 1
fi

echo "Cleaning up..."
rm -rf _site

if [[ "$DEPLOY_COMMAND" == "" ]]; then
    echo "Error: Given jekyll command. Exiting..."
    exit 1
fi

echo "Running bundle install..."
bundle install

echo "Building..."
eval $DEPLOY_COMMAND

echo "Deploying to $DEPLOY_DIR ..."
rsync -avhz -c --delete _site/ "$DEPLOY_DIR" # local deploy
echo "Deployed to $DEPLOY_DIR !"
