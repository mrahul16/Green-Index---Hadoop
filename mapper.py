#!/usr/bin/env python

import sys

total = 0
green = 0

# input comes from STDIN (standard input)
for line in sys.stdin:

    line = line.strip()
    rgb = line.split(',')

    # print '%s\t%d' % ("green", 100)

    if len(rgb) > 0:
        r, g, b = rgb
        total += 1

        if int(g) > int(r) and int(g) > int(b):
            # print '%s\t%d' % ("green", 100)
            green += 1

# if total == 0 :
#     # print(1)
#     print '%s\t%d' % ("green", 1)

if total != 0:
    print '%s\t%f' % ("green", float(green) / float(total))
    # print (float(green) / float(total))
