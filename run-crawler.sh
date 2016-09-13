#!/bin/bash

python crawler.py $1 $2 | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2 | ./reporter.py
