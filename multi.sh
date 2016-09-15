#!/bin/bash

set -e
set -o pipefail

rm -rf "$(pwd)/.tmp/tweets.txt" &> /dev/null || true
mkdir "$(pwd)/.tmp"  &> /dev/null || true

. envs.sh
./crawler.py "$1" "$2" &> "$(pwd)/.tmp/tweets.txt";

cat "$(pwd)/.tmp/tweets.txt" | ./mapper.py | sort -k1,1 | ./reducer.py | sort -nk2 | ./reporter.py "$2" | sort -nk2