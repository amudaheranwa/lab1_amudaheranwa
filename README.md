# lab1_amudaheranwa
# Lab 1 – Grade Evaluator And Archiver

This is my submission for Lab 1. It has two parts: a Python script that checks a students grades and works out their Grade Point Average and a bash script that archives the old grades file so you can start fresh with an one.

## Files in this repository

- `grade-evaluator.py` – reads grades.csv checks the scores and weights are valid works out the Grade Point Average decides if the student passed or failed and tells you which assignments can be resubmitted.

- `organizer.sh` – moves the current grades.csv into an archive folder with a timestamp on it creates a blank grades.csv so you are ready to start the next round of grades.

## Running grade-evaluator.py

Make sure grades.csv is, in the folder then run the Grade Evaluator script.

It will ask you for the filename, type `grades.csv` then it will print out:

- the summative and formative percentage scores

- the final grade and Grade Point Average

- whether the student passed or failed

- any assignments that need to be resubmitted if they failed a formative assignment.

## Running organizer.sh

The time you run it make the script executable.

The Organizer script will create an `archive/` folder if there is not one already move the current grades.csv in there with a timestamp added to the name make an empty grades.csv and log what it did in organizer.log. The Grade Evaluator and Archiver scripts are now ready to use.
