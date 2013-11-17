#include <string.h>
#include <stddef.h>
#include <stdio.h>

size_t
strlength(char const *string)
{
    int length = 0;

    while(*string++ != '\0') length++;

    return length;
}

char*
my_strrstr(char const *s1, char const *s2)
{
    register char* last;
    register char* current;
    last = NULL;

    if (*s2 != '\0') {
        current = strstr(s1, s2);
        
        while (current != NULL) {
            last = current;
            current = strstr(last + 1, s2);
        }
    }

    return last;
}

void print_tokens(char *line)
{
    static char whitespace[] = " \t\f\r\v\n";
    char *token;

    for (token = strtok(line, whitespace); token != NULL;
         token = strtok(NULL, whitespace))
    {
        printf(" Next token is %s\n", token);
    }
}

int main()
{
    char *fsp = "fsp";
    char *fsp1 = "fsp1";
    printf("length1 %zu\n", strlength(fsp));
    if (strlength(fsp) - strlength(fsp1))
    {
        printf("test\n");
    }

    char string[] = "Hello there, honey.";
    char *ans;
    ans = strchr(string, 'h');

    char token_test[] = "fsp is a good student!";
    print_tokens(token_test);
}
