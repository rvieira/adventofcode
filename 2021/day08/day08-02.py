#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:31:36 2021

@author: ricardovieira
"""

count=0
natural_seg = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
curr_seg = ['','','','','','','','','','']
segments = ['','','','','','','']

def same_chars(str1,str2):
    if len(str1) != len(str2):
        return False
    for letter in str1:
        if letter not in str2:
            return False
    return True

def str_contains(str1,str2):
    for letter in str1:
        if letter not in str2:
            return False
    return True

def find_1(line):
    # find the element with 2 digits
    for x in line.split():
        if len(x) == 2:
            return x

def find_4(line):
    # find the element with 4 digits
    for x in line.split():
        if len(x) == 4:
            return x
    
def find_7(line):
    # find the element with 3 digits
    for x in line.split():
        if len(x) == 3:
            return x
        
def find_8(line):
    # find the element with 7 digits
    for x in line.split():
        if len(x) == 7:
            return x

def find_2(line):
    # len() == 5
    # after find_3 and find_5
    for x in line.split():
        if len(x) ==5 and x != curr_seg[3] and x != curr_seg[5]:
            return x

def find_3(line):
    # len() == 5 and only one with 1 (cf)
    for x in line.split():
        if len(x) == 5 and str_contains(curr_seg[1],x):
            return x

def find_5(line):
    # len() == 5
    # find_6 needs to be executed first
    for x in line.split():
        if len(x) == 5 and str_contains(x,curr_seg[6]):
            return x

def find_6(line):
    # len() == 6
    for x in line.split():
        if len(x) == 6 and not str_contains(curr_seg[1],x):
            return x
    
def find_9(line):
    # I have to find the segment with len() == 6 and all segments of 4
    # find_4 has to be executed first to populate curr_seg[4]
    for x in line.split():
        if len(x) == 6 and str_contains(curr_seg[4],x):
            return x

def find_0(line):
    # len() == 6
    for x in line.split():
        if len(x) == 6 and not str_contains(x,curr_seg[6]) and not str_contains(x,curr_seg[9]):
            return x
        
def resolve(line):
    i = 0
    value = ''
    for x in line.split():
        j = 0
        for y in curr_seg:
            if same_chars(x,y):
                value+=str(j)
            j +=1
        i+=1    
    return value

sum = 0
for line in open("input.txt"):
    curr_seg = ['','','','','','','','','','']
    left,right = line.split(' | ')
    curr_seg[1] = find_1(left)
    curr_seg[4] = find_4(left)
    curr_seg[7] = find_7(left)
    curr_seg[8] = find_8(left)
    
    curr_seg[3] = find_3(left)
    curr_seg[6] = find_6(left)
    curr_seg[5] = find_5(left)
    curr_seg[9] = find_9(left)
    curr_seg[0] = find_0(left)
    curr_seg[2] = find_2(left)
#    print(curr_seg)
    digits = resolve(right)
    # print(digits)
    sum += int(digits)
print(sum)

"""
lets call the elements a..g

 aaa
b   c
b   c
b   c
 ddd
e   f
e   f
e   f
 ggg
 
1 = lenght == 2 : 1 = 'cf'
7 = length == 3 : 7 = 'acf'
8 = length == 7 : 9 = 'abcdefg'
4 = length == 4 : 4 = 'bcdf'

0 = "acbefg"
2 = "acdeg"
3 = "acdfg"
5 = "abdfg"
6 = "abdefg"
9 = "abcdfg"

a = 7 - 1
g = 3 - (7+g)

Como as letras mudam, mapeamos o esquema acima aas letras de cada linha, depois de reconhece-las atraves dos algarismos 2,3,4,7, identificados pelo tamaho dos codigos em cada linha.
assim:
    1- uma sequencia de dois caracteres eh "1" (ainda nao seia posicao)
    2- uma sequencia de 3 caracteres contem os do "1" mais "a" (aqui identificamos a caracter "a")
    3- o "4" contem "1" mais "b" e "d". "9" - "g" + "a"

Depois de identificar 1 e 7, a = elems(7) - elems(1)
Entao g = 9 - 4 - a
4 = 9 - a - g

"""