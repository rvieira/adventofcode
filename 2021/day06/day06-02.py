#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 01:03:27 2021

@author: ricardovieira
"""

"""
Each lumpfish created will generate 1 more every 6 days (from the 8th day) 80
= t/6 - init
where t is the time remaining in days

put fishes in buckets according to the age

"""
lumpfishes=[1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]
num_days=256

bucket = []
def count_fish_age(age):
    count = 0
    for i in range(len(lumpfishes)):
        if lumpfishes[i] == age:
            count+=1
    return count

def shift_left():
    save_0 = bucket[0]
    for i in range(1,9):
        bucket[i-1]=bucket[i]
    bucket[8] = save_0    
    bucket[6] = bucket[6] + save_0        

for i in range(9):
    bucket.append(count_fish_age(i))

for i in range(num_days):
    shift_left()  
    print(bucket)

total_lumpfishes = 0
for i in range(len(bucket)):
    total_lumpfishes += bucket[i]
    
print(total_lumpfishes)