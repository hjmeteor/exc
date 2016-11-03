#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
max_token = 0
max_line = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    line_num = 0
    token_num = 0
    for token in tokens:
        token_num = len(token)
        if token_num > max_token:
            max_token = token_num
    if len(line) > max_line:
        max_line = len(line)
print("{0}\t{1}".format(max_token, max_line))
