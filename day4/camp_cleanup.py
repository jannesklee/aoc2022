#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('input.txt') as f:
    lines = f.readlines()

    common_cleanups = 0
    common_overlaps = 0
    for line in lines:
        line = line.strip()
        split_line = line.split(',')
        split_first = split_line[0].split('-')
        split_second = split_line[1].split('-')
        set_elve1 = set(range(int(split_first[0]),int(split_first[1])+1))
        set_elve2 = set(range(int(split_second[0]),int(split_second[1])+1))
        if set_elve1.issubset(set_elve2) or set_elve2.issubset(set_elve1):
            common_cleanups += 1

        if set_elve1.intersection(set_elve2):
            common_overlaps +=1


print(common_cleanups)
print(common_overlaps)
