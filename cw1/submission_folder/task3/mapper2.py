#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
for line in sys.stdin:
    line = line.strip()
    max_t, max_line = line.split("\t")
    if line != '':
        print("{0}\t{1}".format(max_t, max_line))