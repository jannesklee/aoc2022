#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('input.txt') as f:
    lines = f.readlines()

    Score = 0
    for line in lines:
        line = line.split()
        if line[1]=="X":
            Score += 1
        elif line[1]=="Y":
            Score += 2
        elif line[1]=="Z":
            Score += 3

        if line[0]=="A" and line[1]=="X":
            Score += 3
        if line[0]=="A" and line[1]=="Y":
            Score += 6
        if line[0]=="A" and line[1]=="Z":
            Score += 0
        if line[0]=="B" and line[1]=="X":
            Score += 0
        if line[0]=="B" and line[1]=="Y":
            Score += 3
        if line[0]=="B" and line[1]=="Z":
            Score += 6
        if line[0]=="C" and line[1]=="X":
            Score += 6
        if line[0]=="C" and line[1]=="Y":
            Score += 0
        if line[0]=="C" and line[1]=="Z":
            Score += 3

print("The score for part 1 is " + str(Score))


with open('input.txt') as f:
    lines = f.readlines()

    Score = 0
    for line in lines:
        line = line.split()
        if line[1]=="X":
            Score += 0
            if line[0]=="A":
                Score +=3
            elif line[0]=="B":
                Score +=1
            elif line[0]=="C":
                Score +=2
        elif line[1]=="Y":
            Score += 3
            if line[0]=="A":
                Score +=1
            elif line[0]=="B":
                Score +=2
            elif line[0]=="C":
                Score +=3
        elif line[1]=="Z":
            Score += 6
            if line[0]=="A":
                Score +=2
            elif line[0]=="B":
                Score +=3
            elif line[0]=="C":
                Score +=1

print("The score for part 2 is " + str(Score))
