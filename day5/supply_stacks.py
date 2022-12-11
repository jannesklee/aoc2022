#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from abc import ABC, abstractmethod

def read_header(lines: list) -> (list, int):
    for line_number, line in enumerate(lines):
        if line.startswith(' 1 '):
            end_of_header = line_number
            stack_numbers = [int(entry) for entry in re.findall(r' \d+ ', line)]
    return (stack_numbers, end_of_header)

def create_stacks(lines: list, stack_numbers: list, end_of_header: int) -> list:
    stack = [[] for stack_entry in stack_numbers]
    for line in lines[end_of_header-1::-1]:
        splitted_line = [line[i:i+4] for i in range(0, len(line), 4)]
        for stack_number in stack_numbers:
            crate = splitted_line[stack_number-1].strip()
            crate = crate[crate.find("[")+1:crate.find("]")]
            if crate != '':
                stack[stack_number-1].append(crate)
    return stack

# distinguish between different movers with classes
class CrateMover(ABC):
    @abstractmethod
    def move_crates(self, stack: list, movement: dict):
        pass

class CrateMover9000(CrateMover):
    def move_crates(self, stack: list, movement: dict):
        for _ in range(movement['amount']):
             item_to_move = stack[movement['origin']-1].pop()
             stack[movement['destination']-1].append(item_to_move)
        return stack

class CrateMover9001(CrateMover):
    def move_crates(self, stack: list, movement: dict):
        items_to_move = stack[movement['origin']-1][-movement['amount']:]
        del stack[movement['origin']-1][-movement['amount']:]
        stack[movement['destination']-1].extend(items_to_move)
        return stack

def crate_movements(lines: list, end_of_header: int, 
                    stack: list, mover: CrateMover) -> list:
    for line in lines[end_of_header+2:]:
        moving  = re.findall(r' \d+', line)
        amount = int(moving[0])
        origin = int(moving[1])
        destination = int(moving[2])

        movement = {'amount': amount,
                    'origin': origin,
                    'destination': destination}

        crates = mover.move_crates(stack, movement)

    return stack
 

# part 1
with open('input.txt') as f:
    lines = f.readlines()

    stack_numbers, end_of_header = read_header(lines)

    stack = create_stacks(lines, stack_numbers, end_of_header)
   
    MuddyMover = CrateMover9000()
    stack = crate_movements(lines, end_of_header, stack, MuddyMover)

    # get last items
    result_list = []
    for single_stack in stack:
        result_list.append(single_stack[-1])

    print("Part 1 results: ", result_list)


# part 2
with open('input.txt') as f:
    lines = f.readlines()

    stack_numbers, end_of_header = read_header(lines)

    stack = create_stacks(lines, stack_numbers, end_of_header)
   
    MuddyMover = CrateMover9001()
    stack = crate_movements(lines, end_of_header, stack, MuddyMover)

    # get last items
    result_list = []
    for single_stack in stack:
        result_list.append(single_stack[-1])

    print("Part 2 results: ", result_list)



