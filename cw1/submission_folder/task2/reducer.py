#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

prev_sentence = ""
sentence = ""
value_total = 0

for line in sys.stdin:
    line = line.strip()
    sentence, value = line.split("\t")
    value = int(value)
    if value_total == 1 and prev_sentence != sentence:
        print("{0}".format(prev_sentence))
    if prev_sentence != sentence:
        prev_sentence = sentence
        value_total =  value
    else:
        value_total += value
if value_total == 1:
    print("{0}".format(sentence))

