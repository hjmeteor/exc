#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''
prev_que_id = ''
count = 0
que_id = []

max_count = 0
max_que_id = []
max_usr_id = []

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] !=  previd:
        if previd:
            if count == max_count:
                max_que_id.append(que_id)
                max_usr_id.append(previd)
            elif count > max_count:
                max_que_id = []
                max_usr_id = []
                max_count = count
                max_que_id.append(que_id)
                max_usr_id.append(previd)
            count = 0
            que_id = []
        previd = tokens[0]
    
    for n in range(int(tokens[1])):
        if tokens[2 + n] != prev_que_id:
            que_id.append(tokens[2 + n])
            prev_que_id = tokens[2 + n]
            count += 1


if count == max_count:
    max_que_id.append(que_id)
    max_usr_id.append(previd)
elif count > max_count:
    max_que_id = []
    max_usr_id = []
    max_count = count
    max_que_id.append(que_id)
    max_usr_id.append(previd)

for n in range(len(max_usr_id)):
    print("{0} ->".format(max_usr_id[n])),
    for m in range(max_count):
        if m == max_count - 1:
            print("{0}".format(max_que_id[n][m]))
        else:
            print("{0},".format(max_que_id[n][m])),

del que_id[:]
del max_que_id[:]
del max_usr_id[:]