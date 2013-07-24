#include<iostream>
#include<stdlib.h>
using namespace std;

struct node
{
    int item;
    struct node* next;
    node(int x, struct node* t)
    {
        item = x;
        next = t;
    }
};
struct node2
{
    int item;
    struct node2* next;
};
typedef struct node* nodeLink;
typedef struct node2* nodeLink2;
typedef int Item;
// One global link node
nodeLink2 freelist;

void construct(int N)
{
    freelist = new node2[N+1];
    for (int i = 0; i < N; i++)
        freelist[i].next = &freelist[i+1];
    freelist[N].next = 0;
}

nodeLink2 remove(nodeLink2 x)
{
    nodeLink2 t = x->next;
    x->next = t->next;
    return t;
}
nodeLink2 newNode(int i)
{
    nodeLink2 x = remove(freelist);
    x->item = i;
    x->next = x;
    return x;
}

void insert(nodeLink2 x, nodeLink2 t)
{
    t->next = x->next;
    x->next = t;
}
void deleteNode(nodeLink2 x)
{
    insert(freelist, x);
}
nodeLink2 next(nodeLink2 x)
{
    return x->next;
}
Item item(nodeLink2 x)
{
    return x->item;
}

void visit(int item)
{
    cout<< item << endl;
}

void traverse(nodeLink head)
{
    nodeLink t;
    visit(head->item);
    for (t = head->next; t != head; t = t->next)
        visit(t->item);
}

void traverse_0(nodeLink head)
{
    nodeLink t;
    for (t = head; t != 0; t = t->next)
        visit(t->item);
}

nodeLink reverse(nodeLink head)
{
    nodeLink t, r = new node(1, 0), k, y, tmp;
    r->next = head;
    for (t = head->next; t != head;)
    {
        k = t;
        y = r->next;
        r->next = t;
        t = t->next;
        k->next = y;
    }
    head->next = r->next;
    tmp = r->next;
    delete(r);
    return tmp;
}

int main(int argc, char* argv[])
{
    //int i, N = atoi(argv[1]), M = atoi(argv[2]);
    int i, N = 9, M = 5;
    nodeLink t = new node(1, 0);
    t->next = t;
    nodeLink x = t;
    for (i = 2; i <= N; i++)
        x = (x->next = new node(i, t));
    while (x != x->next)
    {
        for (i=1; i < M; i++) x = x->next;
        x->next = x->next->next;
    }
    cout << x->item <<endl;
    cout << "Initializing the linked list....................................."<<endl;
    x = t;
    for (i = 2;i <= 10; i++)
        x = (x->next = new node(i, t));
    cout << "Traverse........................................................."<<endl;
    traverse(t);
    cout << "After reverse...................................................."<<endl;
    t = reverse(t);
    traverse(t);
    node heada(0, 0);
    nodeLink a = &heada, h = a;
    for (int i = 0; i < 10; i++)
        h = (h->next = new node(rand() % 1000, 0));
    cout << "Insertion Sort..................................................."<<endl;
    traverse_0(heada.next);
    node headb(0, 0);
    nodeLink u, x2, b = &headb, h2;
    for (h2 = a->next; h2 != 0; h2 = u)
    {
        u = h2->next;
        for (x2 = b; x2->next != 0; x2 = x2->next)
            if (x2->next->item > h2->item) break;
        h2->next = x2->next;
        x2->next = h2;
    }
    cout << "After Sort......................................................."<<endl;
    traverse_0(headb.next);
}
