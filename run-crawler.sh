#!/bin/bash

python crawler.py | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2
