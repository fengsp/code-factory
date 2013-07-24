#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;

int lg(int);
int lg(int N)
{
    int i = 0;
    for (; N > 2; N /= 2) i++;
    return i;
}


typedef int Number;
Number randNum()
{
    return rand();
}


typedef struct point { float x; float y; } point;
float distance(point, point);
struct point a, b;
float m_distance(point a, point b)
{
    float dx = a.x - b.x, dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}


static const int N = 1000;


int heads()
{
    return rand() < RAND_MAX/2;
}
float randFloat()
{
    return 1.0*rand()/RAND_MAX;
}

int main(int argc, char *argv[])
{
    for (int N = 1000; N <= 1000000000; N *= 10)
        cout << lg(N) << " " << N << endl;
    
    if (argc < 2)
    {
        cout << "Please type in loop num: " << endl;
        exit(0);
    }
    int N = atoi(argv[1]);
    float m1 = 0.0, m2 = 0.0;
    for (int i = 0; i < N; i++)
    {
        Number x = randNum();
        m1 += ((float) x)/N;
        m2 += ((float) x*x)/N;
    }
    cout << "Argument:" << argv[0] << " " << argv[1] << endl;
    cout << "    Avg.:" << m1 << endl;
    cout << "Std.dev.:" << sqrt(m2-m1*m1) << endl;

    a.x = 1.0; a.y = 1.0;
    b.x = 4.0; b.y = 5.0;
    cout << "Distance is: " << m_distance(a, b) << endl;

    int i;
    int *a = new int[N];
    for (i = 2; i < N; i++) a[i] = 1;
    for (i = 2; i < N; i++)
    {
        if (a[i])
           for (int j = i; j*i < N; j++) a[i*j] = 0;
    }
    for (i = 2; i < N; i++)
        if (a[i]) cout << " " << i;
    cout << endl;

    int j, cnt;
    N = 30;
    int M = 5000;
    int *f = new int[N+1];
    for (j = 0; j <= N; j++) f[j] = 0;
    for (i = 0; i < M; i++, f[cnt]++)
        for (cnt = 0, j = 0; j <= N; j++)
            if (heads()) cnt++;
    for (j = 0; j <= N; j++)
    {
        if (f[j] == 0) cout << ".";
        for (i = 0; i < f[j]; i+=10) cout << "*";
        cout << endl;
    }
    
    N = 1000; float d = 10.0;
    point *points = new point[N];
    for (i=0; i < N; i++)
    {
        points[i].x = randFloat(); points[i].y = randFloat();
    }
    for (i = 0; i < N; i++)
        for (j = i+1; j < N; j++)
            if (m_distance(points[i], points[j]) < d) cnt ++;
    cout << cnt << " pairs within " << d << endl;

    return 0;
}

