#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

    sumval = 0
    elvebox = [];
    for line in lines:
        if line=='\n':
            elvebox.append(sumval)
            sumval = 0
        else:
            sumval += int(line)

# Part 1
elvecalories = np.max(elvebox)
elvenumber = np.argmax(elvebox)

print("Elve with number " + str(elvenumber) + " carries " + str(elvecalories) + " calories.")

# Part 2
elvebox_sorted = sorted(elvebox)
print(elvebox_sorted[-3:])
print("The top 3 elves carry " + str(sum(elvebox_sorted[-3:])))

