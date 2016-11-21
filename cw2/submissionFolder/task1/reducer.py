#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

prev_word = ""
prev_doc = ""
word = ""
docs = []
values = []

for line in sys.stdin:
    line = line.strip()
    if line != "":
        word, doc, value = line.split()
    value = int(value)

    if prev_word == word:
        if prev_doc == doc:
            values[-1] += value
        else:
            prev_doc = doc
            docs.append(doc)
            values.append(value)

    elif prev_word != word:
        if prev_word:
            docs_len = len(docs)
            if docs_len == 1:
                print("{0} : {1} : {{({2}.txt, {3})}}".format(prev_word, 1, docs[0], values[0]))
            else:
                print("{0} : {1} :".format(prev_word, docs_len)),
                for n in range(docs_len):
                    if n == docs_len - 1:
                        print("({0}.txt, {1})}}".format(docs[n], values[n]))
                    elif n == 0:
                        print("{{({0}.txt, {1}),".format(docs[n], values[n])),
                    else:
                        print("({0}.txt, {1}),".format(docs[n], values[n])),
            docs = []
            values = []
        prev_word = word
        prev_doc = doc
        values.append(value)
        docs.append(doc)

if prev_word == word:
    docs_len = len(docs)
    if docs_len == 1:
        print("{0} : {1} : {{({2}.txt, {3})}}".format(prev_word, 1, docs[0], 1))
    else:
        print("{0} : {1} :".format(prev_word, docs_len)),
        for n in range(docs_len):
            if n == docs_len - 1:
                print("({0}.txt, {1})}}".format(docs[n], values[n]))
            elif n == 0:
                print("{{({0}.txt, {1}),".format(docs[n], values[n])),
            else:
                print("({0}.txt, {1}),".format(docs[n], values[n])),
else:
    print("{0} : {1} : {{({2}.txt, {3})}}".format(word, 1, doc, 1))

del docs[:]
del values[:]
