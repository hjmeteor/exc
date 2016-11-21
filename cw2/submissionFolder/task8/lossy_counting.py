#!/usr/bin/env python

import sys

D = {}
current_w = 1
count = 0
del_key = []
w_size = 1.0/0.001

for line in sys.stdin:
    line = line.strip()
    count += 1

    if line in D:
        D[line][0] += 1

    else:
        d = [1, current_w -1]
        D[line] = d

    if count % w_size == 0:
        for item in D:
            if D[item][0]+D[item][1] <= current_w:
                del_key.append(item)
        for index in range(len(del_key)):
            del D[del_key[index]]

        del_key = []
        current_w += 1

for item in D:
    if D[item][0] >= (0.01 - 0.001) * count:
        print(item)