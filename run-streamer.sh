#!/bin/bash

python streamer.py $1 $2 $3 | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2
