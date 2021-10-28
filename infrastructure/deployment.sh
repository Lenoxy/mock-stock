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



$VERSION=$(grep "VERSION=" docker-compose.env | cut -d '=' -f 2)

echo "$VERSION"

git pull origin master

docker-compose down

cd ./backend
pip install -r requirements.txt
cd ..

cd ./frontend
npm install
npm run build
cd ..

docker-compose -d --force-recreate --build --env-file ./docker-compose.env up
