#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:43:22 2021

@author: ricardovieira
"""


"""
1- read input
2- loop
    1- increase energy
    2- flashes
        1- increase energy of adjacent octopi
        2- flashes
    3- flashed octopus -> energy 0
    
        
"""

def print_matrix():
    for line in lines:
        print(line)
    print()

def increase(lin,pos):
    if lin >=0 and lin <len(lines) and pos>=0 and pos < len(lines[lin]):
        if lines[lin][pos] != 'f':
            if int(lines[lin][pos]) < 9:
                lines[lin] = lines[lin][:pos]+str(int(lines[lin][pos]) + 1)+lines[lin][pos+1:]
            else:
                lines[lin] = lines[lin][:pos]+'f'+lines[lin][pos+1:]
                flash(lin,pos)
        
def flash(lin,pos):
    
    global flash_count
    flash_count += 1
    increase(lin-1,pos-1)
    increase(lin-1,pos)
    increase(lin-1,pos+1)
    increase(lin,pos-1)
    increase(lin,pos+1)
    increase(lin+1,pos-1)
    increase(lin+1,pos)
    increase(lin+1,pos+1)
    
 
def read_lines():
    for line in open("input.txt"):
        lines.append(line.strip())
        
def process_step():
    for i in range(len(lines)):
        for j in range (len(lines[i])):
            increase(i,j)
    for i in range(len(lines)):
        for j in range (len(lines[i])):
            if lines[i][j] == 'f':
                lines[i] = lines[i][:j]+'0'+lines[i][j+1:]
            
flash_count = 0
octopuses = []
lines = []
steps=100

read_lines()
#print(lines)
for i in range(steps):
    process_step()
#    print_matrix()
print(flash_count)