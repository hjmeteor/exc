#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if tokens[0] == 'student':
        print("{0}\t{1}\t{2}\t{3}".format(tokens[1], tokens[0], tokens[2], 0))
    else:
        print("{0}\t{1}\t{2}\t{3}".format(tokens[1], tokens[0], tokens[2],
                                          tokens[3]))