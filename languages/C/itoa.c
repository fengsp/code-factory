#include <stdio.h>
#include <stdarg.h>
#include <string.h>

void binary_to_ascii(unsigned int value)
{
    unsigned int quotient;
    quotient = value / 10;
    if(quotient != 0)
        binary_to_ascii(quotient);
    putchar( value % 10 + '0');
}

float
average(int n_values, ...)
{
    va_list var_arg;
    int count;
    float sum = 0;

    va_start(var_arg, n_values);

    for(count = 0; count < n_values; count += 1)
    {
        sum += va_arg(var_arg, int);
    }

    va_end(var_arg);

    return sum / n_values;
}

void arr_test()
{
    int array[] = {1, 2, 3, 4, 5};
    int *a;
    a = &array[0];
    printf("sizeof a: %lu\n", sizeof(a));
    for(int i = 0; i < sizeof(array) / sizeof(int); i++)
    {
        printf("array index for %d: %d\n", i, a[i]);
    }
    printf("OMG: %d\n", 3[array]); // Oh my God!!!
}

void string_copy(char *buffer, char const *string)
{
    while((*buffer++ = *string++) != '\0')
        ;
}

int
lookup_keyword(char const * const desired_word, char const *keyword_table[], int const size)
{
    char const **kwp;
    for(kwp = keyword_table; kwp < keyword_table + size; kwp++)
    {
        if(strcmp(desired_word, *kwp) == 0)
            return kwp - keyword_table;
    }
    return -1;
}

int main()
{
    unsigned int value = 10000;
    binary_to_ascii(value);
    printf("\n");
    
    float avg = average(5, 1, 2, 3, 4, 5);
    printf("The average is %f\n", avg);

    arr_test();
}
