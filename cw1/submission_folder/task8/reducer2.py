#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

max_average = [0.0]
max_student = [0.0]

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if float(tokens[1]) == float(max_average[-1]):
        max_student.append(tokens[0])
        max_average.append(tokens[1])
    if float(tokens[1]) > float(max_average[-1]):
        max_student = []
        max_average = []
        max_average.append(tokens[1])
        max_student.append(tokens[0])
for n in range(len(max_student)):
    print("{0}".format(max_student[n]))