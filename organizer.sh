#!/bin/bash

if [ ! -d "archive" ]; then
    mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")
new_filename="grades_${timestamp}.csv"
 
mv grades.csv "archive/${new_filename}"
 
touch grades.csv
 
echo "${timestamp} | original: grades.csv | archived as: archive/${new_filename}" >> organizer.log
 
echo "Archived grades.csv as archive/${new_filename}"
