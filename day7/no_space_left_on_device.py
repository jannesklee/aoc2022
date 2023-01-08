#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def find_unique_key(key, dictionary):
    if key in dictionary.keys():
        key = key + "_"
        if key in dictionary.keys():
            key = find_unique_key(key, dictionary)

    return key

with open('input.txt') as f:
    lines  = f.readlines()

    foldersize = {};
    current_dir_list  = [];

    for line in lines:
        line = line.strip()
        lineparts = [x.strip() for x in line.split(' ')]

        if lineparts[0]=='$':
            command = lineparts[1]
            if command=='cd':
                dir_name = lineparts[2]
                if dir_name=='..':
                    current_dir_list.pop()
                else:
                    unique_key = find_unique_key(dir_name, foldersize)
                    current_dir_list.append(unique_key)
                    foldersize[unique_key] = 0;
            elif lineparts[1]=='ls':
                pass
            else:
                raise Exception("The incoming command is not known.")
        else:
            if lineparts[0]=='dir':
                pass
            elif lineparts[0].strip().isnumeric:
                size_of_file = int(lineparts[0])
                for foldername in current_dir_list:
                    foldersize[foldername] = \
                            foldersize[foldername] + size_of_file
            else:
                raise Exception("The incoming folder structure is not known.")

total_sum=0
for foldername in foldersize:
    if foldersize[foldername] <= 100000:
        total_sum = total_sum + foldersize[foldername]

print("Result of part 1: ", total_sum)

total_disk_size = 70000000
update_size = 30000000
total_used_space = foldersize['/']
needed_space = update_size - (total_disk_size - total_used_space)

possible_folders = []
for foldername in foldersize:
    if foldersize[foldername] >= needed_space:
        possible_folders.append(foldersize[foldername])

print("Result of part 2: ", min(possible_folders))


