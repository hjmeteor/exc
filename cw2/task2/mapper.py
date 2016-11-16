#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
# precompiled regular expressions
re_question_viewcounts = re.compile(r'^(<row\sId)(=")(\d+)(".*?)(PostTypeId="1")(.*?)(ViewCount=")(\d+)(".*\s/>)$')
for line in sys.stdin:
    line = line.strip()
    m = re_question_viewcounts.match(line)
    if m != None:
        record = m.groups()
        print("{0}\t{1}".format(record[7], record[2]))
