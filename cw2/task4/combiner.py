#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''
count = 0
ans_id = []

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] !=  previd:
        if previd:
            print("{0}\t{1}".format(previd, count)),
            for m in range(len(ans_id)):
                if m == count - 1:
                    print("{0}".format(ans_id[m]))
                else:
                    print("{0}".format(ans_id[m])),
            count = 0
            ans_id = []
        previd = tokens[0]
    for n in range(int(tokens[1])):
        ans_id.append(tokens[2 + n])
    count += int(tokens[1])

print("{0}\t{1}".format(previd, count)),
for m in range(len(ans_id)):
    if m == count - 1:
        print("{0}".format(ans_id[m]))
    else:
        print("{0}".format(ans_id[m])),

del ans_id[:]
