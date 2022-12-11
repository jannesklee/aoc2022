#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def get_starting_index(char_string: str, amount_marker: int) -> (int, str):
    for idx in range(amount_marker-1,len(char_string)+1):
        current_string = char_string[idx-(amount_marker-1):idx+1]
        freq = Counter(current_string)

        if(len(freq) == len(current_string)):
            start_index = idx+1
            return (start_index, current_string)

with open('input.txt') as f:
    char_string = f.readlines()
    char_string = char_string[0].strip()

    start_index_package, current_string = get_starting_index(char_string, 4)
    start_index_message, current_string = get_starting_index(char_string, 14)

    print("The characters that need to be processed are:", start_index_package)
    print("The characters that need to be processed are:", start_index_message)
