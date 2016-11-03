#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
num = 0
for line in sys.stdin:
    line = line.strip()
    if num < 20:
        value, sentence = line.split("\t")
        print("{0}\t{1}".format(value, sentence))
        num += 1
