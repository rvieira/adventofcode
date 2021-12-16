#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:25:16 2021

@author: ricardovieira
"""

def valid_coords(coords):
    return coords[0].split(',')[0] == coords[2].split(',')[0] or coords[0].split(',')[1] == coords[2].split(',')[1]

def plot_line(coords):
    x1 = int(coords[0].split(',')[0])
    y1 = int(coords[0].split(',')[1])
    x2 = int(coords[2].split(',')[0])
    y2 = int(coords[2].split(',')[1])
    if x1 == x2:
        if y1 < y2:
            for i in range(y1,y2+1):
                matrix[x1][i] += 1
        else:
            for i in range(y2,y1+1):
                matrix[x1][i] += 1
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1,x2+1):
                matrix[i][y1] += 1
        else:
            for i in range(x2,x1+1):
                matrix[i][y1] += 1
    
    elif abs(x2-x1) == abs(y2-y1): # need to use the module
        for i in range(abs(x2-x1)+1):
            if (x1<x2 and y1<y2):
                matrix[x1+i][y1+i] += 1
            elif (x1<x2 and y1>=y2):
                matrix[x1+i][y1-i] += 1
            elif (x1>=x2 and y1<y2):
                matrix[x1-i][y1+i] += 1
            else:
                matrix[x1-i][y1-i] += 1

def populate_matrix():
    for line in open("input.txt"):
        coords = line.split()
#        if valid_coords(coords):
        plot_line(coords)
#        print(x[0],x[1],x[2])
#        print(x)
        
def count_greater_than_2():
    count = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if matrix[i][j] > 1:
                count += 1
    return count
            
    
if __name__ == '__main__':
    num_rows = num_columns = 1000
    matrix = [[0 for x in range(num_rows)] for y in range(num_columns)]
    populate_matrix()
#    print(matrix)
    print(count_greater_than_2())