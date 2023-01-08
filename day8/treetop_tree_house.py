#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

with open('input.txt') as f:
    lines  = f.readlines()

    size_dim_1 = (len(lines))
    size_dim_2 = len(lines[0].strip())
    tree_height = np.zeros((size_dim_1, size_dim_2), dtype=np.int8)
    visible_trees  = np.zeros((size_dim_1, size_dim_2), dtype=bool)

    for lineidx, line in enumerate(lines):
        tree_height[lineidx,:] = [int(x) for x in line.strip()]


for idx in range(1,size_dim_1-1):
    for jdx in range(1,size_dim_2-1):
        western_dir = all(tree_height[idx,jdx] > tree_height[idx,:jdx])
        eastern_dir = all(tree_height[idx,jdx] > tree_height[idx,jdx+1:])
        northern_dir = all(tree_height[idx,jdx] > tree_height[:idx,jdx])
        southern_dir = all(tree_height[idx,jdx] > tree_height[idx+1:,jdx])
        visible_trees[idx, jdx] = any(\
                np.array([western_dir, eastern_dir, northern_dir, southern_dir]))

visible_trees[0,:] = True
visible_trees[-1,:] = True
visible_trees[:,0] = True
visible_trees[:,-1] = True

print(sum(sum(visible_trees)))
