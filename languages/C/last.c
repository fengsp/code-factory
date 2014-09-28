#include <stdlib.h>
#include <stdio.h>

#define NAME_LENGTH 30
#define ADDR_LENGTH 100
#define PHONE_LENGTH 11
#define MAX_ADDRESSES 1000

char const *
lookup_address(char const *name);
char const *
lookup_phone(char const *name);

static char name[MAX_ADDRESSES][NAME_LENGTH];
static char address[MAX_ADDRESSES][ADDR_LENGTH];
static char phone[MAX_ADDRESSES][PHONE_LENGTH];

static int
find_entry(char const *name_to_find)
{
    int entry;

    for(entry=0; entry < MAX_ADDRESSES; entry += 1)
    {
        if(strcmp(name_to_find, name[entry]) == 0)
            return entry;
    }
    return entry;
}

char const*
lookup_address(char const *name)
{
    int entry;
    entry = find_entry(name);
    if(entry == -1)
        return NULL;
    else
        return address[entry];
}

char const*
lookup_phone(char const *name)
{
    int entry;
    entry = find_entry(name);
    if(entry == -1)
        return NULL;
    else
        return phone[entry];
}

int
even_parity(int value, int n_bits)
{
    int parity = 0;

    while( n_bits > 0 ) {
        parity += value & 1;
        value >>= 1;
        n_bits -= 1;
    }

    return ( parity % 2 ) == 0;
}

void swap(int *x, int *y)
{
    int tmp;

    tmp = *x;
    *x = *y;
    *y = tmp;
}

int main()
{
    int a = 1;
    int b = 2;
    swap(&a, &b);
    printf("%d => %d\n", a, b);
}
