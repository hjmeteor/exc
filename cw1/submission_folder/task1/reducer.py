#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
for line in sys.stdin:
    line = line.strip()
    line = line.upper()
    print("{0}".format(line))
