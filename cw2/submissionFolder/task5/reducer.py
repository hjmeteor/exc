#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import random

line_number = 0
line = ''
sum_lines = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')
    line = tokens[0]
    line_number = int(tokens[1])
    sum_lines += line_number
    if random.randint(0, sum_lines - 1) < line_number :
        resevoir = line
print('{0}'.format(resevoir))
