#!/bin/sh
export FLASK_APP=./nba_stat_track/index.py
pipenv run flask --debug run -h 0.0.0.0 -p 5001
