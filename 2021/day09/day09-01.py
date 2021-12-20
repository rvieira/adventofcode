#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 03:04:27 2021

@author: ricardovieira
"""

lines = []
low_points = []

def is_low_point(x,y):
    # check up
    if y > 0 and lines[y-1][x] <= lines[y][x]:
        return False
    # check down
    if y < len(lines)-1 and lines[y+1][x] <= lines[y][x]:
        return False
    # check left
    if x > 0 and lines[y][x-1] <= lines[y][x]:
        return False
    # check right
    if x < len(lines[y])-1 and lines[y][x+1] <= lines[y][x]:
        return False
    return True
    
sum_risk = 0

for line in open("input.txt"):
    lines.append(line.strip())
    
#print(lines)
for y in range(len(lines)): 
    for x in range(len(lines[y])):
        if is_low_point(x,y):
            low_points.append((x,y))
for low_point in low_points:
#    print (lines[low_point[1]][low_point[0]])
    sum_risk += int(lines[low_point[1]][low_point[0]]) + 1
print(sum_risk)