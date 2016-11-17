#!/usr/bin/env python
from bitarray import bitarray
import mmh3
import sys
import math


class BloomFilter:
    def __init__(self, bitarray_num, hash_num):
        self.bitarray_num = bitarray_num
        self.hash_num = hash_num
        self.bit_array = bitarray(bitarray_num)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in xrange(self.hash_num):
            result = mmh3.hash(string, seed) % self.bitarray_num
            self.bit_array[result] = 1

    def query(self, string):
        for seed in xrange(self.hash_num):
            result = mmh3.hash(string, seed) % self.bitarray_num
            if self.bit_array[result] == 0:
                return False
        return True


def get_num(false_positive_probility, entries):
    bit_p_key = math.ceil(-(math.log(false_positive_probility, 2) / math.log(2)
                            ))
    bitarray_num = bit_p_key * float(entries)
    hash_num = math.ceil(bit_p_key * math.log(2))
    return (int(bitarray_num), int(hash_num))


if __name__ == '__main__':
    false_positive_probility = 0.01
    num = get_num(false_positive_probility, sys.argv[1])
    bf = BloomFilter(num[0], num[1])
    for line in sys.stdin:
        line = line.strip()
        if bf.query(line) is False:
            bf.add(line)
            print("{0}".format(line))
