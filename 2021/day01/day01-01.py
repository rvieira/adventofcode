#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:33:52 2021

@author: ricardovieira
"""

previous_depth=-1
i=0

for line in open('input.txt'):
    depth=int(line)
    if depth > previous_depth:
        i+=1
    previous_depth=depth
print(i-1)