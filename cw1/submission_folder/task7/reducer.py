#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

student_name = ""
count = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[1] == 'student' and count != 0:
        student_name = tokens[2]
        print("\r")
        print("{0}-->".format(tokens[2])),
    if tokens[1] == 'student' and count == 0:
        student_name = tokens[2]
        print("{0}-->".format(tokens[2])),
        count += 1
    if tokens[1] == "mark":
        print("({0},{1} )".format(tokens[2], tokens[3])),