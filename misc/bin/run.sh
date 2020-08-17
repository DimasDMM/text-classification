#!/bin/bash

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source ${SCRIPT_PATH}/environment-vars.sh

$SCRIPT_PATH/down.sh

cd $SCRIPT_PATH/../../
docker-compose -f docker-compose.yml -p $PROJECT_USER up -d --build
cd -

# Initialize database and import datasets
idocker python_${PROJECT_USER} sh ./misc/bin/indocker/wait-postgresql.sh
idocker python_${PROJECT_USER} sh ./misc/bin/indocker/database-creation.sh
idocker python_${PROJECT_USER} python ./misc/bin/indocker/etl.py
