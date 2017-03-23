#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >= 3:
        fuel = line[2]
        cylinders = line[3]
        print '%s\t%s' % (fuel, cylinders)



