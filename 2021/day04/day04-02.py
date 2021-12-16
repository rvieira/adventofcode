#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:20:50 2021

@author: ricardovieira
"""

num_boards=100
num_columns = num_rows = 5
boards = [[[0 for x in range(num_rows)] for y in range(num_columns)] for z in range(num_boards)]
marked = [[[False for x in range(num_rows)] for y in range(num_columns)] for z in range(num_boards)]
winning_boards = [False for x in range(num_boards)]

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

def mark_board(board_num,num):
    for i in range(num_rows):
        for j in range(num_columns):
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

def mark_winning_board(board_num):
    winning_boards[board_num] = True

def mark_winning_boards():
    for i in range(num_boards):
        if check_board(i):
            mark_winning_board(i)
   
def last_board():
    winning_count = 0
    for i in range(num_boards):
        if winning_boards[i]:
            winning_count += 1
    if winning_count == num_boards-1:
        for i in range(num_boards):
            if not winning_boards[i]:
                return i
    elif winning_count == num_boards:
        return -2        
    return -1

def calculate_score(board_num):
    score = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if not marked[board_num][i][j]:
                score += int(boards[board_num][i][j])
    score = score*int(aux_numbers[num_drwan_numbers])
    return score

# def let_looser_win():
    
    
if __name__ == '__main__':
    str_numbers=''
    lines=[]
    load_boards()
    aux_numbers = str_numbers.split(',')
    for num_drwan_numbers in range(len(aux_numbers)):
        mark_all_boards(aux_numbers[num_drwan_numbers])
        mark_winning_boards()
        aux_looser = last_board()
        if aux_looser != -1:
            if aux_looser == -2:
                break
            else:
                looser = aux_looser
    print(calculate_score(looser))
