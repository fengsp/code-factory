#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

class POINT
{
    private:
        float x, y;
    public:
        POINT()
        {
            x = 1.0*rand()/RAND_MAX;
            y = 1.0*rand()/RAND_MAX;
        }
        float distance(POINT a)
        {
            float dx = x-a.x, dy = y-a.y;
            return sqrt(dx*dx + dy*dy);
        }
        static float distance2(POINT a, POINT b)
        {
            float dx = a.x - b.y, dy = a.y - b.y;
            return sqrt(dx*dx + dy*dy);
        }
        float X() const
        {
            return x;
        }
        float Y() const
        {
            return y;
        }
        friend int operator==(POINT a, POINT b)
        {
            return distance2(a, b) < .001;
        }
        friend ostream& operator<<(ostream& t, POINT p)
        {
            cout << "(" << p.X() << "," << p.Y() << ")";
            return t;
        }
};

template<class Item>
class STACK
{
    private:
    public:
        STACK(int);
        int empty() const;
        void push(Item item);
        Item pop();
};

int main(int argc, char* argv[])
{
    float d = atof(argv[2]);
    int i, cnt = 0, N = atoi(argv[1]);
    POINT *a = new POINT[N];
    for (i = 0; i < N; i++)
        for (int j = i+1; j < N; j++)
            if (a[i].distance(a[j]) < d) cnt++;
    cout << cnt << " pairs within " << d << endl;
}
