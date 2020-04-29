#!/bin/bash

MANAGER_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $MANAGER_DIR
case $1 in
  docker:run)
    ${MANAGER_DIR}/misc/bin/run.sh
    ;;
  docker:down)
    ${MANAGER_DIR}/misc/bin/down.sh
    ;;
  python)
    ${MANAGER_DIR}/misc/bin/python-container.sh
    ;;
  train)
    ${MANAGER_DIR}/misc/bin/python-container.sh train
    ;;
  predict)
    ${MANAGER_DIR}/misc/bin/python-container.sh predict "$2"
    ;;
  *)
    echo "Error: The command does not exist!!"
    exit 1
    ;;
esac
