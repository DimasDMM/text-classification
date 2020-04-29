#!/bin/bash

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Including .env file
set -o allexport
source $SCRIPT_PATH/../../.env
set +o allexport

# Add variable
export PROJECT_USER="${PROJECT_NAME}_${USER}"
