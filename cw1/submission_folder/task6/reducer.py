#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import math

two_words = ''
last_word = ''
prev_two_words = ''
count = []
same = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    two_words = ' '.join(tokens[0:2])
    last_word = ''.join(tokens[2])
    count.append(tokens[3])
    if prev_two_words == two_words:
        same += 1
        # print('%s : %d' % (line, same))
    else:
        # print('2')
        if prev_two_words and same == 0:
            print("{0} {1}".format(prev_two_words, 0))
        elif prev_two_words and same >= 1:
            entropy_context = 0.0
            probability = []
            sum_count = 0.0

            for n in range(same + 1):
                sum_count += float(count[-(2 + n)])
            for n in range(same + 1):
                probability.append((float(count[-(2 + n)]) / sum_count))
                entropy_context += -(float(probability[n] *
                                            math.log(probability[n], 2)))
            print("{0} {1}".format(prev_two_words, entropy_context))
            same = 0
        prev_two_words = two_words
if same == 0:
    print("{0} {1}".format(prev_two_words, 0))
else:
    sum_count = 0.0
    entropy_context = 0.0
    probability = []
    sum_count = 0.0
    for n in range(same + 1):
        sum_count += float(count[-(2 + n)])
    for n in range(same + 1):
        probability.append((float(count[-(2 + n)]) / sum_count))
        entropy_context += -(float(probability[n] * math.log(probability[n], 2)))
    print("{0} {1}".format(prev_two_words, entropy_context))

