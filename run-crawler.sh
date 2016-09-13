#!/bin/bash

./crawler.py "$1" | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2 | ./reporter.py | sort -nk2
