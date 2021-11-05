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

echo "shutting down docker containers"

docker-compose --env-file docker-compose.env down

git reset --hard
git pull origin master

docker-compose --env-file docker-compose.env up -d --build --force-recreate

CURRENT_VERSION="$(grep "VERSION=" ./../docker-compose.env | cut -d '=' -f 2)"
NEXT_VERSION="$(($CURRENT_VERSION + 1))"

echo $CURRENT_VERSION
echo $NEXT_VERSION

BACKEND_CONTAINER="$(docker ps -q -f name="mock-stock-backend" -f status="running")"
FRONTEND_CONTAINER="$(docker ps -q -f name="mock-stock-frontend" -f status="running")"

if [ -z "$BACKEND_CONTAINER" ] || [ -z "$FRONTEND_CONTAINER"];
then
    echo "[BACKEND] shutting down"
    docker stop mock-stock-backend-$CURRENT_VERSION
    docker rm -f mock-stock-backend-$CURRENT_VERSION
    echo "[BACKEND] offline"

    echo "[FRONTEND] shutting down"
    docker stop mock-stock-frontend-$CURRENT_VERSION
    docker rm -f mock-stock-frontend-$CURRENT_VERSION
    echo "[FRONTEND] offline"

    docker-compose -d --force-recreate --build --env-file ./docker-compose.env up

else
    echo "[BACKEND] removing old image"
    docker rm -f mock-stock-backend-$PREVIOUS_VERSION
    docker image rm -f mock-stock-backend-$PREVIOUS_VERSION
    echo "[Backend] old image is gone"

    echo "[FRONTEND] removing old image"
    docker rm -f mock-stock-backend-$PREVIOUS_VERSION
    docker image rm -f mock-stock-backend-$PREVIOSU_VERSION
    echo "[FRONTEND] old image is gone"

    rm -f docker-compose.env
    echo VERSION=$NEXT_VERSION  > /home/mock-stock/mock-stock/docker-compose.env
    git commmit -m "VERSION UPDATE"
    git push

fi






