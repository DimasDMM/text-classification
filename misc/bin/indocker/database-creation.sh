#!/bin/bash

psql -h $DB_HOST -p $DB_INTERNAL_PORT -U $DB_USER -c "SET TIME ZONE 'UTC';" --quiet
psql -h $DB_HOST -p $DB_INTERNAL_PORT -U $DB_USER -c "DROP DATABASE IF EXISTS $DB_DBNAME;" --quiet
psql -h $DB_HOST -p $DB_INTERNAL_PORT -U $DB_USER -c "CREATE DATABASE $DB_DBNAME ENCODING 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';" --quiet

echo "Database has been created correctly"

exit 0
