#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:57:40 2021

@author: ricardovieira
"""

previous_depth=-1
i=count_deeper=0
depth=[]

for line in open('input.txt'):
    depth.append(int(line))
    i+=1
for j in range(3,i):
    previous_window=depth[j-3]+depth[j-2]+depth[j-1]
    current_window=depth[j-2]+depth[j-1]+depth[j]
    if current_window > previous_window:
        count_deeper += 1
print(count_deeper)