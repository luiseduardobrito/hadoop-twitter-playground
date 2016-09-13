#!/bin/bash

set -e
set -o pipefail

. envs.sh
python streamer.py $1 | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2
