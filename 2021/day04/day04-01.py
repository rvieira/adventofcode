#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:00:47 2021

@author: ricardovieira
"""

num_boards=100 
num_columns = num_rows = 5
boards = [[[0 for x in range(num_rows)] for y in range(num_columns)] for z in range(num_boards)]

def load_boards():
    global str_numbers
    global boards
    board_num=0
    line_num=0
    with open("input.txt") as f:
        str_numbers = f.readline().strip()
        f.readline() # reads empty line
        line = f.readline().strip()
        while line:
            if line == '':
                board_num += 1
                line_num=0
            else:
                boards[board_num][line_num] = line.split()
                line_num += 1
            line = f.readline().strip()
               
#def read_board():
    
def load_lines():
    for line in open("input.txt"):
        lines.append(line.strip())
        
if __name__ == '__main__':
    str_numbers=''
    lines=[]
    load_boards()
    print(str_numbers)
    print(boards)

    print(lines)