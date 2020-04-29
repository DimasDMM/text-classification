#!/bin/bash

echo "Connection to Postgresql..."
sleep 5

while ! pg_isready -h $DB_HOST -p $DB_INTERNAL_PORT -U $DB_USER --quiet
do
    sleep 5
    echo "Retrying in 5 seconds..."
done

echo "Postgresql is ready"

exit 0
