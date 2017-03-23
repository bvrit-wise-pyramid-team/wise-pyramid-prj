#!/usr/bin/python
#Reducer.py
import sys

def cylinders():
    fuel_cylinders = {}
    for line in sys.stdin:
        line = line.strip()
        fuel,cylinders = line.split('\t')

    if fuel in fuel_cylinders:
        fuel_cylinders[fuel].append(int(cylinders))
    else:
        fuel_cylinders[cylinders] = []
        fuel_cylinders[cylinders].append(int(cylinders))

    for fuel in fuel_cylinders.keys():
        ave_cylinders = sum(fuel_cylinders[fuel])*1.0 / len(fuel_cylinders[fuel])
        print("{}\t{}".format(fuel, ave_cylinders)

cylinders()
