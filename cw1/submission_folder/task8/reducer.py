#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

prev_studentId = ''
max_average = [0.0]
max_student = [0.0]
average = 0.0
sum_score = 0.0
count = 0.0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    studentId = tokens[0]

    if studentId != prev_studentId:
        if tokens[1] == "mark":
            average = 0.0
            sum_score = 0.0
            count = 0.0
            sum_score += float(tokens[3])
            count += 1
    if studentId == prev_studentId:
        if tokens[1] == "mark":
            sum_score += float(tokens[3])
            count += 1
        elif tokens[1] == "student" and count > 3:
            average = float(sum_score / count)
            if average > max_average[-1]:
                max_student = []
                max_average = []
                max_average.append(average)
                max_student.append(tokens[2])
                prev_studentName = tokens[2]
            elif average == max_average[-1]:
                max_average.append(average)
                max_student.append(tokens[2])
            average = 0.0
            sum_score = 0.0
            count = 0.0
    prev_studentId = studentId
for n in range(len(max_student)):
    print("{0}\t{1}".format(max_student[n], max_average[n]))

