// Created on Fri Dec 30 13:12:02 2021
//
// @author: ricardovieira
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int previous_depth=-1;
    int i=0, depth;
    char line[10];
    FILE* file = fopen("/Users/ricardovieira/github/adventofcode/2021/day01/input.txt", "r");

    while (fgets(line, 10, file)) {
        depth = atoi(line);
        if (depth > previous_depth) i++;
        previous_depth = depth;
    }
    printf("%i\n", i-1);
    fclose(file);
}