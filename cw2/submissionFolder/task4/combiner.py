#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''
count = 0
flag = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] == '1':
        if tokens[1] !=  previd:
            if previd:
                print("{0} {1}\t{2}".format(1, previd, count))
                count = 0
            previd = tokens[1]
        count += int(tokens[2])
    else:
        if flag == 0:
            print("{0} {1}\t{2}".format(1, previd, count))
            flag = 1
        print("{0} {1}\t{2}".format(2, tokens[1], tokens[2]))
