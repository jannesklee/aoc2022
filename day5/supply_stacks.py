#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open('input.txt') as f:
    lines = f.readlines()

    # read header to find out number of stacks
    for line_number, line in enumerate(lines):
        if line.startswith(' 1 '):
            end_of_header = line_number
            stack_numbers = [int(entry) for entry in re.findall(r' \d+ ', line)]

    # create stacks
    stack = [[] for stack_entry in stack_numbers]
    for line in lines[end_of_header-1::-1]:
        splitted_line = [line[i:i+4] for i in range(0, len(line), 4)]
        for stack_number in stack_numbers:
            crate = splitted_line[stack_number-1].strip()
            crate = crate[crate.find("[")+1:crate.find("]")]
            if crate != '':
                stack[stack_number-1].append(crate)
    
    # movements on stacks
    for line in lines[end_of_header+2:]:
        moving  = re.findall(r' \d+', line)
        amount = int(moving[0])
        origin = int(moving[1])
        destination = int(moving[2])
        for _ in range(amount):
            item_to_move = stack[origin-1].pop()
            stack[destination-1].append(item_to_move)

    # get last items
    result_list = []
    for single_stack in stack:
        result_list.append(single_stack[-1])

    print(result_list)

        

