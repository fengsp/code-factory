#include<iostream>
#include<stdlib.h>
using namespace std;

char demo[] = "fsp is a boy!";
char *demo2;
char demo3[] = "fsp is a";
static const int N = 10000;

int strlen(char* a)
{   
    int i;
    for(i=0; a[i] != 0; i++);
    return i;
}

void strcpy(char* a, char* b)
{
    int i;
    for(i=0; (a[i] = b[i]) != 0; i++);
}

int strcmp(char* a, char* b)
{
    while(*a++ == *b++)
        if(*(a-1) == 0) return 0;
    return *(a-1) - *(b-1);
}

void strcat(char* a, char* b)
{
    strcpy(a+strlen(a), b);
}

int main(int argc, char* argv[])
{
    cout << "strlen():   " << strlen(demo) << endl;
    demo2 = new char('a');
    strcpy(demo2, demo);
    cout << "strcpy():   " << demo2 << endl;
    cout << strcmp(demo, demo3) << endl;
    char *test = new char('a');
    cout << *test-0 << endl;
    strcat(demo, demo2);
    cout << "strcat():   " << demo << endl;
    cout << "searching............................." << endl;
    int i; char t;
    char a[N], *p = argv[1];
    for (i = 0; i < N-1; a[i] = t, i++)
        if (!cin.get(t)) break;
    a[i] = 0;
    for (i = 0; a[i] != 0; i++)
    {
        int j;
        for (j = 0; p[j] != 0; j++)
            if (a[i+j] != p[j]) break;
        if (p[j] == 0) cout << i << " ";
    }
    cout << endl;
}
