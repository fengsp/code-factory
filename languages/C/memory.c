#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

#define MALLOC(num, type) (type*)alloc((num) * sizeof(type))

void *
alloc(size_t size)
{
    void *new_memory;
    new_memory = malloc(size);
    if (new_memory == NULL) {
        printf("Out of memory!\n");
        exit(1);
    }
    return new_memory;
}

int main()
{
    int *pi;
    pi = malloc(100);
    if (pi == NULL) {
        printf("Out of memory!\n");
        exit(1);
    }

    for (int i = 0; i < 25; i++)
        *pi++ = 0;

    char *test;
    test = MALLOC(20, char);
}
