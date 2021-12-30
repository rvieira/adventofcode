#include <stdio.h>
#include <stdlib.h>

struct Depth {
    int depth;
    struct Depth* next;
};
struct Depth *head = NULL;

void append_depth(int depth) {
    struct Depth *new_node = malloc(sizeof(struct Depth));
    new_node->depth = depth;
    new_node->next = NULL;
    if (head == NULL) {
        head = new_node;
    }
    else {
        struct Depth *last_node = head;
        while (last_node->next != NULL) {
            last_node = last_node->next;
        }
        last_node->next = new_node;
    }
} 

int get_depth(int index) {
    struct Depth *current_depth = head;
    int i;

    for (i=1;i<index;i++) {
        current_depth = current_depth->next;
    }
    return current_depth->depth;
}

void free_list() {
    struct Depth *tmp;
    while (head != NULL) {
        tmp = head;
        head = head->next;
        free(tmp);
    }
}

int main()
{
    int previous_depth=-1, i=0, j, count_deeper=0, previous_window, current_window;
    char line[10];

    FILE* file = fopen("/Users/ricardovieira/github/adventofcode/2021/day01/input.txt", "r");

    /*head = NULL;*/

    while (fgets(line,10,file)) {
        append_depth(atoi(line));        
        i++;
    }
    for (j=3;j<i;j++) {
        previous_window = get_depth(j-3)+get_depth(j-2)+get_depth(j-1);
        current_window = get_depth(j-2)+get_depth(j-1)+get_depth(j);
        if (current_window > previous_window) count_deeper++;
    }
    printf("%i\n",count_deeper);
    free_list();
}