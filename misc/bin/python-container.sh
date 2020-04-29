#!/bin/bash

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source ${SCRIPT_PATH}/environment-vars.sh

if [ $1 == 'train' ]
then
    docker exec -it python_${PROJECT_USER} python ./code/main.py -t
elif [ $1 == 'predict' ]
then
    docker exec -it python_${PROJECT_USER} python ./code/main.py -p "$2"
else
    docker exec -it python_${PROJECT_USER} bash
fi
