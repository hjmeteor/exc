#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import heapq

count = 1
q = []
# precompiled regular expressions
re_question_viewcounts = re.compile(r'^(<row\sId)(=")(\d+)(".*?)(PostTypeId="1")(.*?)(ViewCount=")(\d+)(".*\s/>)$')
for line in sys.stdin:
    line = line.strip()
    m = re_question_viewcounts.match(line)
    if m:
        ViewCount = m.groups()[7]
        QuestionId = m.groups()[2]
        entry = [int(ViewCount), QuestionId]
        if(count > 10):
            heapq.heappushpop(q, entry)
        else:
            heapq.heappush(q, entry)
            count += 1
for n in range(10):
    record = heapq.heappop(q)
    print("{0}\t{1}".format(record[0], record[1]))

del q[:]
