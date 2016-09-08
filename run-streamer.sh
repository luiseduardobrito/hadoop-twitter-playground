#!/bin/bash

python streamer.py | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2
