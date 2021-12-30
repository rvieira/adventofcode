#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:43:22 2021

@author: ricardovieira
"""
lines=[]
matrix=[]

def find_max_lines():
    max_x = 0
    max_y = 0
    for line in lines:
        try:
            strx, stry = line.split(",")
            x = int(strx)
            y = int(stry)
        except ValueError:
            break
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return max_x, max_y

def insert_sharp(x,y):
    if x < (len(matrix[y])) and x>0:
        aux = matrix[y][:x-1]+"#"+matrix[y][x+1:]
        matrix[y] = matrix[y][:x-1]+"#"+matrix[y][x+1:]
    elif x == 0:
        aux = "#" + matrix[y][1:]
        matrix[y] = "#"+matrix[y][1:]
    else:
        aux = matrix[y][:x-1]+"#"
        matrix[y] = matrix[y][:x-1]+"#"
        
def fill_matrix():
    global matrix
    
    max_x, max_y = find_max_lines()
    empty_line = ""
    for i in range(max_x):
        empty_line += "." 
    matrix=[empty_line for x in range(max_y)]
    # print(empty_line)
#    for line in lines:
#        if "fold" not in line:
#            x, y = line.split(",")
#            insert_sharp(int(x),int(y))
            
#    for line in lines:
#        if "fold" not in line and line != '':
#           x, y = line.split(",")
#            matrix.append(x+"|"+y)
        
def read_first_instruction():
    return("fold along x=655")

def fold(direction,pos):
    result = matrix.copy()
    if direction == "y":
        print("y")
    else:
        print("x")
    print(pos)
    # fold x
    for line in matrix:
        for i in range(int(pos),len(line)):
            if line[i] == "#" or line[pos+i] == "#":
                line = line[:pos-i]+"#"+line[pos+i:]
            else:
                line = line[:pos-i]+"."+line[pos+i:]
        result.append(line[:pos])
        # so far I am only removing the extra columns
    return result
   
     

def read_lines():
    for line in open("input.txt"):
        lines.append(line.strip())


read_lines()
instruction = read_first_instruction()
try:
    direction = instruction[instruction.index("=")-1]
    position = instruction[instruction.index("=")+1:]
except ValueError:
    raise
fill_matrix()
insert_sharp(0,0)
insert_sharp(0,1)
insert_sharp(1,1)
fold(direction,position)
print( matrix )
#print(lines)