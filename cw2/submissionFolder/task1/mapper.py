#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import re
# precompiled regular expressions
re_doc = re.compile(r'^(.*/)(.+)(.txt)$')
for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    loc = os.environ["mapreduce_map_input_file"]
    doc = re_doc.match(loc).groups()[1]
    for token in tokens:
        print("{0} {1} {2}".format(token, doc, 1))
