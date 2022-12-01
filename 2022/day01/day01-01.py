#!/usr/bin/env python3
"""
Created on Thu 01 Dec 2021

@author: ricardovieira
"""

curr_elf_total=0
elf=[]

for line in open('input.txt'):
    if line=='\n':
        elf.append(curr_elf_total)
        curr_elf_total=0
    else:
        curr_elf_total+=int(line)
elf.sort()
#print(elf)
print(elf[-1])
print(elf[-1]+elf[-2]+elf[-3])