#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

prev_doc = ""
prev_word = ""
word = ""
value_total = 0
docs = ""

for line in sys.stdin:
    line = line.strip()
    word, doc, value = line.split()
    value = int(value)
    if prev_doc == doc and prev_word == word:
        value_total += value
    elif prev_doc!= doc and prev_word ==word:
        print("{0} {1} {2}".format(word, prev_doc, value_total))
        value_total = value
        prev_doc = doc
        prev_word = word
    else:
        if prev_word:
            print("{0} {1} {2}".format(prev_word, prev_doc, value_total))
        value_total = value
        prev_doc = doc
        prev_word = word

print("{0} {1} {2}".format(word, doc, value_total))
