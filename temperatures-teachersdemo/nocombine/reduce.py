#!/usr/bin/python3
import fileinput
city = None
total = 0.0
samples = 0
for line in fileinput.input():
    new_city, observation = line.strip().split('\t')
    if new_city != city:
        if city:
            print(city, total / samples, sep='\t')
        city = new_city
        total = 0.0
        samples = 0
    total += float(observation)
    samples += 1
if city:
    print(city, total / samples, sep='\t')