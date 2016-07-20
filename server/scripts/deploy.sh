#!/bin/bash

#
# Variables
#

REPO_DIR="$1"
GIT_BRANCH="$2"
TARGET_PATH="$3"
IS_TESTING="$4"

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

git checkout -f $GIT_BRANCH
sleep 1
git reset --hard HEAD
git pull origin $GIT_BRANCH

if [ ! -d "$TARGET_PATH" ]; then
    echo "An error has occurred! Check your target path and try again. Aborting..."
    exit 1
fi

echo "Cleaning up..."
rm -rf _site

if [[ "$IS_TESTING" == "stable" ]]; then
    jekyll build
elif [[ "$IS_TESTING" == "testing" ]]; then
    jekyll build --drafts --future
else
    echo "Error: Given task is neither 'stable' or 'testing'. Exiting..."
    exit 1
fi

echo "Deploying to $TARGET_PATH ..."
rsync -avhz -c --delete _site/ "$TARGET_PATH" # local deploy
echo "Deployed to $TARGET_PATH !"
