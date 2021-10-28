#!/bin/bash
echo Deployment Script

cd /home/mock-stock/mock-stock || exit

# pull release
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != "master" ]]; then
  echo 'Aborting script, wrong branch';
  echo "$BRANCH";
  exit 1;
fi

# clear any changes (possibly package-lock.json)
git reset --hard

git pull origin master

docker-compose down

cd ./backend
pip install -r requirements.txt
cd ..

cd ./frontend
npm install
npm run build
cd ..

docker-compose up -d --force-recreate --build --env-file ./docker-compose.env
