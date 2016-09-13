#!/usr/bin/env python
import sys
from pprint import pprint

current_word = None
current_count = 0
word = None

d = {"jdoriajr": 0, "celsorussomanno": 0}

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    try:

        # convert count (currently a string) to int
        count = int(count)

    except ValueError:

        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if word in d:
        d[word] += count

total = 0

for key, value in d.iteritems():
    total += float(value)

for key, value in d.iteritems():
    print key + ': ' + str("%0.2f" % float(value / total))
