#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

sequence = []
count = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    line_num = 0
    tokens_len = len(tokens)
    for n in range(tokens_len - 2):
        sequence = []
        sequence = " ".join(tokens[n:n + 3])
        print("{0}\t{1}".format(sequence, 1))
