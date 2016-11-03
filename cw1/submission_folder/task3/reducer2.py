#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
max_token = 0
max_line = 0

for line in sys.stdin:
    line = line.strip()
    max_t, max_l = line.split("\t")
    max_t = int(max_t)
    max_l = int(max_l)
    if max_t > max_token:
        max_token = max_t
    if max_l > max_line:
        max_line = max_l
print("{0}\t{1}".format(max_token, max_line))
    