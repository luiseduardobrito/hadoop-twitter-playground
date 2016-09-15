#!/bin/bash

set -e
set -o pipefail

. envs.sh
./crawler.py "$1" "$2" | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2 | ./reporter.py "$2" | sort -nk2
