#!/usr/bin/env python
import json
import re
import sys
from unicodedata import normalize

word = None
total = 0
d = {}

# Get query from command line
if len(sys.argv) < 2:
    print "No query term specified."
    print "Usage: ./reporter.py <usa|sao-paulo>"
    sys.exit(1)

# Get script arguments
cand_data = sys.argv[1]

# Read candidates file
with open('./input/' + cand_data + '.json') as data_file:
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

if total > 0:

    # Calculate proportions
    for key, value in d.iteritems():
        print key + ': ' + str("%0.2f" % float(value / total))

else:
    print "No results to report"
