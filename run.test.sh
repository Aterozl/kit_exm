#!/bin/bash
NAME="`whoami`/`date '+%Y-%m-%d/%T'`"
COVERAGE_DIR=".coverage_response/$NAME"

find -P ./ -iname '*.pyc' -delete
export PYTHONPATH=.:app:$PYTHONPATH
nosetests ./tests/* --with-coverage --cover-tests --cover-html --cover-html-dir $COVERAGE_DIR --cover-package=app
