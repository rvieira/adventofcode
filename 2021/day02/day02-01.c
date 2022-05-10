#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int h_pos=0,depth=0;
char command[3]={"forward","up","down"};

int main() {
    char line[11], str_command[10], str_value[4];
    int int_value;
    FILE* file = fopen("/Users/ricardovieira/github/adventofcode/2021/day02/input.txt", "r");

    while (fgets(line, 10, file)) {
        strcpy(str_command, strsep(line, " "));
        strcpy(str_value, strsep(NULL, " "));
        int_value = atoi(str_value);
        if (str_command == command[0]) h_pos += atoi(int_value);
        if (str_command == command[1]) depth += atoi(int_value);
        if (str_command == command[2]) depth -= atoi(int_value);
    }
    printf("%i\n", h_pos*depth);
    fclose(file);
}