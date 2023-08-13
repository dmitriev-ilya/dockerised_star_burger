#!/bin/bash
set -Eeuo pipefail

git pull

docker-compose -f docker-compose-prod.yml build
docker-compose -f docker-compose-prod.yml up -d

source ./.env
git_commit=$(git -C ./ rev-parse HEAD)

curl -H "X-Rollbar-Access-Token:$ROLLBAR_TOKEN" -H "Content-Type: application/json" -X POST 'https://api.rollbar.com/api/1/deploy'\
 -d '{"environment":"'$ROLLBAR_ENVIRONMENT'", "revision":"'$git_commit'", "rollbar_name":"'$ROLLBAR_NAME'", "local_username":"'$USER'", "comment": "", "status": "succeeded"}'

echo
echo "The deployment was successful!"
