#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import random

line_number = []
lines = []
sum_lines = 0.0

for line in sys.stdin:
    tokens = line.split('\t')
    lines.append(tokens[0])
    line_number.append(tokens[1])
for n in line_number:
    sum_lines += int(n)

for n in range(len(lines)):
    if random.randint(0, sum_lines) < line_number :
        resevoir = lines[n].strip()
print('{0}'.format(resevoir))
