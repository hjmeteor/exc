#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''
prev_que_id = ''
count = 0
que_id = []

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] !=  previd:
        if previd:
            print("{0} {1}".format(previd, count)),
            for m in range(len(que_id)):
                if m == count - 1:
                    print("{0}".format(que_id[m]))
                else:
                    print("{0}".format(que_id[m])),
            count = 0
            que_id = []
        previd = tokens[0]
    for n in range(int(tokens[1])):
        if tokens[2 + n] != prev_que_id:
            que_id.append(tokens[2 + n])
            prev_que_id = tokens[2 + n]
            count += 1

print("{0} {1}".format(previd, count)),
for m in range(len(que_id)):
    if m == count - 1:
        print("{0}".format(que_id[m]))
    else:
        print("{0}".format(que_id[m])),

del que_id[:]