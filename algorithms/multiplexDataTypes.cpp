#include<iostream>
#include<stdlib.h>
using namespace std;

int **malloc2d(int r, int c)
{
    int **t = new int*[r];
    for(int i = 0; i < r; i++)
        t[i] = new int[c];
    return t;
}
void print(int **a, int r, int c)
{
    int i, j;
    for(i = 0; i < r; i++)
    {
        for(j = 0; j < c; j++)
            cout << a[i][j] << " | ";
        cout << endl;
        for(j = 0; j < c * 6 - 2; j++)
            cout << "-";
        cout << endl;
    }
}

int generate()
{
    int i;
    while((i = rand() % 1000) < 100);
    return i;
}

int main(int argc, char* argv[])
{
    int **demo = malloc2d(4, 6);
    int **demo2 = malloc2d(6, 4);
    int **demo3 = malloc2d(4, 4);
    int i, j, k;
    for(i = 0; i < 4; i++)
        for(j=0; j < 6; j++)
            demo[i][j] = generate();
    for(i = 0; i < 6; i++)
        for(j=0; j < 4; j++)
            demo2[i][j] = generate();
    cout << "demo..." << endl;
    print(demo, 4, 6);
    cout << "demo2..." << endl;
    print(demo2, 6, 4);
    for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
            for(k = 0; k < 6; k++)
                demo3[i][j] += demo[i][k] * demo2[k][j];
    cout << "after matrix product..." << endl;
    print(demo3, 4, 4);
}
