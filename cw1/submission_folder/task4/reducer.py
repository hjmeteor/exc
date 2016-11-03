#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

prev_sentence = " "
sentence = " "
value_total = 0

for line in sys.stdin:
    line = line.strip()
    sentence, value = line.split("\t")
    value = int(value)
    if prev_sentence == sentence:
        value_total += value
    else:
        if prev_sentence and prev_sentence != ' ':
            print("{0}\t{1}".format(prev_sentence, value_total))
        value_total = value
        prev_sentence = sentence
if prev_sentence == sentence:
    print("{0}\t{1}".format(prev_sentence, value_total))