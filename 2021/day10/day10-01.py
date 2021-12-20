#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:52:05 2021

@author: ricardovieira
"""

def matched_pair(line):
    value = line.find('()') 
    if value == -1:
        value = line.find('[]')
        if value == -1:
            value = line.find('{}')
            if value == -1:
                value = line.find('<>')
    return value
        
def remove_matched(line):
    matched_pos = matched_pair(line)
    while matched_pos != -1:
        line = line[:matched_pos]+line[matched_pos+2:]
        matched_pos = matched_pair(line)
    return line

def remove_left_brackets(line):
    value = ''
    for letter in line:
        if letter in ')]}>':
            value += letter
    return value
            
lines=[]
weight = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
error_score = 0
for line in open("input.txt"):
    lines.append(line.strip())
    unmatched_chars = remove_matched(line)
    unmatched_chars = remove_left_brackets(unmatched_chars)
    #if no closing characters, incomplete. closing characters corruption
    if len(unmatched_chars) > 0:
        error_score += weight[unmatched_chars[0]]
print(lines)
print(error_score)