#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 02:23:01 2021

@author: ricardovieira
"""
count=0
for line in open("input.txt"):
#    print(line)
#    print(line.find('|'))
#    print(line[line.find('|')+2:])
    left = line[line.find('|')+2:]
    for x in left.split():
        if len(x) in [2,4,3,7]:
            count+=1
print(count)