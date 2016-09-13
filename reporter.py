#!/usr/bin/env python
import json
import re
import sys
from unicodedata import normalize

data = None
word = None
total = 0
d = {}

# Read candidates file
with open('./input/sao-paulo-sp.json') as data_file:
    data = json.load(data_file)

for cand in data:
    s = re.sub(r'([^\s\w]|_)+', '', normalize('NFKD', cand["screen"]))
    d[s] = 0

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

# Calculate total value
for key, value in d.iteritems():
    total += float(value)

# Calculate proportions
for key, value in d.iteritems():
    print key + ': ' + str("%0.2f" % float(value / total))
