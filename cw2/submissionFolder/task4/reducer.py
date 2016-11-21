#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

previd = ''

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] == previd:
        print("{0} {1}\t{2}".format(1, tokens[2], 1))
        print("{0} {1}\t{2}".format(2, tokens[2], tokens[0]))
    else:
        previd = tokens[0]
