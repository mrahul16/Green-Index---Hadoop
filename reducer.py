#!/usr/bin/env python

from operator import itemgetter
import sys

total = 0
perc_g = 0
g = 0

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    _, g = line.split('\t', 1)

    try:
        g = float(g)
    except ValueError:
        continue

    total += 1
    perc_g += g

if total == 0:
    print '%s' % ("Invalid")

if total != 0:
    print "%s\t%f" % ("green", float(perc_g) / float(total))
