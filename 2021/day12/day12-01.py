#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:41:32 2021

@author: ricardovieira
"""

paths=[]
lines = []

def read_lines():
    for line in open("test.txt"):
        lines.append(line.strip())
    
read_lines()
print(lines)
