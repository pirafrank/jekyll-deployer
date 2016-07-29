#!/bin/bash

API_TOKEN=""
ACTION="deploy"
DEPLOY_TYPE=""

if [[ $# != 1 ]]; then
    echo "Error: wrong number of arguments"
    echo "Usage: ./script.sh [stable|testing]"
    exit 1
fi

if [[ $1 == "stable" ]]; then
    DEPLOY_TYPE="stable"
elif [[ $1 == "testing" ]]; then
    DEPLOY_TYPE="testing"
else
    echo "Error: given parameter is not 'stable' nor 'testing'"
    exit 1
fi

echo "deploying..."
curl \
-H '{"Access-Token":"'"$API_TOKEN"'","Content-Type: application/json"}' \
-X POST \
-d '{"action":"'"$ACTION"'","deploy_type":"'"$DEPLOY_TYPE"'"}' \
https://fpira.com/webhooks/Qe2R70SyKJjFLN # fixme: flask errors
