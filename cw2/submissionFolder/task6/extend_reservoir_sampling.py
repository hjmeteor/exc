#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import random

resevoir = []
line_number = 0
k = 100

for line in sys.stdin:
    line = line.strip()
    if line_number <= k:
        resevoir.append(line)
    else:
        r = random.randint(0, line_number)
        if r < k:
            resevoir[r] = line
    line_number += 1
for n in range(k):
    print('{0}'.format(resevoir[n]))

del resevoir[:]
