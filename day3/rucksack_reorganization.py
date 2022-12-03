#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('input.txt') as f:
    lines = f.readlines()

    priority_1 = 0
    for line in lines:
        line = line.strip()
        linelength = len(line)
        line_begin = line[:int(linelength/2)]
        line_end = line[int(linelength/2):]
        assert line==line_begin+line_end

        common_types = list(set(line_begin)&set(line_end))
        assert len(common_types) == 1

        common_type = common_types[0]
        if common_type.islower():
            priority_1 += ord(common_type)-ord('a') + 1
        elif common_type.isupper():
            priority_1 += ord(common_type)-ord('A') + 27

    priority_2 = 0
    for idx in range(int(len(lines)/3)):
        common_types = list(set(lines[idx*3+0].strip()) & \
                            set(lines[idx*3+1].strip()) & \
                            set(lines[idx*3+2].strip()))
        assert len(common_types) == 1
        common_type = common_types[0]

        if common_type.islower():
            priority_2 += ord(common_type)-ord('a') + 1
        elif common_type.isupper():
            priority_2 += ord(common_type)-ord('A') + 27


print('The priority of task 1 is ' + str(priority_1))
print('The priority of task 2 is ' + str(priority_2))


