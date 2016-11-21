#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''
count = 0
flag = 0
output_count = 0
max_count = 0
max_usr_id = ''

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] == '1':
        if tokens[1] !=  previd:
            if previd:
                if(count > max_count):
                    max_count = count
                    max_usr_id = previd
                count = 0
            previd = tokens[1]
        count += int(tokens[2])
    else:
        if flag == 0:
            if(count > max_count):
                max_count = count
                max_usr_id = previd
            flag = 1
        if max_usr_id == tokens[1]:
            if output_count == 0:
                print("{0} -> {1},".format(max_usr_id, max_count)),
                print("{0},".format(tokens[2])),
                output_count += 1
            elif output_count == max_count - 1:
                print("{0}".format(tokens[2]))
            else:
                print("{0},".format(tokens[2])),
                output_count += 1