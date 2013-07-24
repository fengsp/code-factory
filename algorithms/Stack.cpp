#include<iostream>
#include<stdlib.h>
#include<string>
using namespace std;

template<class Item>
class STACK
{
    private:
        struct node
        {
            Item item;
            struct node* next;
            node(Item x, struct node* t)
            {
                item = x;
                next = t;
            }
        };
        typedef node* link;
        int len;
        link head;
    public:
        STACK(int)
        {
            head = 0;
            len = 0;
        }
        int empty() const
        {
            return head == 0;
        }
        void push(Item x)
        {
            head = new node(x, head);
            len += 1;
        }
        Item pop()
        {
            Item v = head->item;
            link t = head->next;
            delete head;
            head = t;
            len -= 1;
            return v;
        }
        int length() const
        {
            return len;
        }
};

int main(int argc, char* argv[])
{
    char *a = argv[1];
    int N = strlen(a);
    STACK<char> ops(N);
    STACK<char> demo(N);
    STACK<char> demo2(N);
    STACK<int> save(N);
    for(int i = 0; i < N; i++)
    {
        if (a[i] == ')')
            demo.push(ops.pop());
        if ((a[i] == '+') || (a[i] == '*'))
            ops.push(a[i]);
        if ((a[i] >= '0') && (a[i] <= '9'))
            demo.push(a[i]);
    }
    int len = demo.length();
    for(int i = 0; i < len; i++)
    {
        demo2.push(demo.pop());
    }
    // cout << demo2.length() << endl;
    char tmp;
    for(int i = 0; i < len; i++)
    {
        tmp = demo2.pop();
        if (tmp == '+')
        {
            save.push(save.pop() + save.pop());
        }
        if (tmp == '*')
            save.push(save.pop() * save.pop());
        if ((tmp >= '0') && (tmp <= '9'))
        {
            save.push((tmp-'0'));
        }
    }
    cout << save.pop() << endl;
}
/*
./destExe '(5*(((9+8)*(4*6))+7))'
*/
