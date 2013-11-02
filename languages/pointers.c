#include <stdlib.h>
#include <stdio.h>

#define TRUE 1
#define FALSE 0

int test(int test)
{
    //int test;
    return 1;
}

int
m_strlen(char *string)
{
    int length = 0;
    while( *string++ != '\0')
        length++;
    return length;
}

int find_char(char **strings, char value)
{
    char* string;
    while((string = *strings++) != NULL)
    {
        while(*string != '\0')
        {
            if(*string++ == value)
                return TRUE;
        }
    }
    return FALSE;
}

int main()
{
    test(1);
    char* fsp = "fsp";
    char* strings[] = {"fsp", "fsp2", NULL};
    int length = m_strlen(fsp);
    printf("%d\n", length);
    printf("%d\n", find_char(strings, 'f'));
    printf("%d\n", find_char(strings, 'y'));
}
