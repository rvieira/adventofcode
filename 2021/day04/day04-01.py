#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:00:47 2021

@author: ricardovieira
"""

num_boards=100
num_columns = num_rows = 5
boards = [[[0 for x in range(num_rows)] for y in range(num_columns)] for z in range(num_boards)]
marked = [[[False for x in range(num_rows)] for y in range(num_columns)] for z in range(num_boards)]

def load_boards():
    global str_numbers
    global boards
    board_num=0
    line_num=0
    with open("input.txt") as f:
        str_numbers = f.readline().strip()
        f.readline()
        for line in f:
            if line == '\n':
                board_num += 1
                line_num=0
            else:
                boards[board_num][line_num] = line.split()
                line_num += 1
#            line = f.readline().strip()
               
#def read_board():

def mark_board(board_num,num):
    for i in range(num_rows):
        for j in range(num_columns):
 #           print(boards[board_num][i][j])
            if boards[board_num][i][j] == num:
                marked[board_num][i][j] = True
    
def check_board(board_num):
    value = False
    for i in range(num_rows):
        if False not in marked[board_num][i]:
            value = True
    for j in range(num_columns):
        if marked[board_num][0][j] and marked[board_num][1][j] and marked[board_num][2][j] and marked[board_num][3][j] and marked[board_num][4][j]:
            value = True
    return value        
            
#    for number in num_list:
        
    
def load_lines():
    for line in open("input.txt"):
        lines.append(line.strip())
        
def mark_all_boards(number_list):
    for i in range(num_boards):
        mark_board(i,number_list)

def check_all_boards():
    for i in range(num_boards):
        if check_board(i):
            return i
    return -1

def calculate_score(board_num):
    score = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if not marked[board_num][i][j]:
                score += int(boards[board_num][i][j])
    score = score*int(aux_numbers[num_drwan_numbers])
    return score
    
if __name__ == '__main__':
    str_numbers=''
    lines=[]
    load_boards()
    aux_numbers = str_numbers.split(',')
    for num_drwan_numbers in range(len(aux_numbers)):
        mark_all_boards(aux_numbers[num_drwan_numbers])
        winning_board = check_all_boards()
        if winning_board != -1:
            print(winning_board)
            break
    print(calculate_score(winning_board))
#    print(str_numbers)
#    print(boards)
#    mark_board(0,['12','75','58','21','87'])
#    mark_board(0,['12','55','37','72','91'])
#    mark_board(0,['75','80','35','68','60'])
#    print(check_board(0))
#    print(marked)
#    print(lines)