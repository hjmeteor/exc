#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

for line in sys.stdin:
    line = line.strip()
    value, sentence = line.split("\t")
    print("{0}\t{1}".format(value, sentence))