#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:17:28 2021

@author: ricardovieira
"""

lines = []
low_points = []
basins = []
basin_sizes = []

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

def adjacent_points(point):
    if point[0] >= 0 and point[1] >= 0 and point[0] < len(lines[0]) and point[1] < len(lines):
        if point not in basins  and lines[point[1]][point[0]] != '9':
            basins.append(point)
            adjacent_points((point[0]+1,point[1]))
            adjacent_points((point[0]-1,point[1]))
            adjacent_points((point[0],point[1]+1))
            adjacent_points((point[0],point[1]-1))
                         

def basin_size(point):
    basin = []
    basin.append(point)
    #while adjacent_points
    
count = 0

for line in open("input.txt"):
    lines.append(line.strip())
    
#print(lines)
for y in range(len(lines)): 
    for x in range(len(lines[y])):
        if is_low_point(x,y):
            low_points.append((x,y))
for low_point in low_points:
#    print (lines[low_point[1]][low_point[0]])
    basins=[]
    adjacent_points(low_point)
    print(basins)
    count += len(basins)
    basin_sizes.append(len(basins))
maxes = []
for i in range(3):
    _max = max(basin_sizes)
    maxes.append(_max)
    basin_sizes.remove(_max)
result = maxes[0]*maxes[1]*maxes[2]
print(result)