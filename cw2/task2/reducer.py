#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
num = 0
for line in sys.stdin:
    line = line.strip()
    if num < 10:
        ViewCount, QuestionId = line.split()
        print("{0} {1}".format(ViewCount, QuestionId))
        num += 1
