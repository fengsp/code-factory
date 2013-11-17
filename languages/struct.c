#include <stdio.h>

typedef struct {
    int a;
    short b[2];
} Ex2;
typedef struct EX {
    int a;
    char b[3];
    Ex2 c;
    struct EX *d;
} Ex;
typedef struct {
    char product[20];
    int quantity;
    float unit_price;
    float total_amount;
} Transaction;

void print_receipt(Transaction *trans)
{
    printf("%s\n", trans->product);
    printf("%d @ %.2f total %.2f\n", trans->quantity, trans->unit_price, trans->total_amount);
}

union test{
    int a;
    char c[4];
};

int main()
{
    Ex x = {10, "Hi", {5, {-1, 25}}, 0};
    Ex *px = &x;
    int ha;
    ha = 10;

    Transaction fsp = {
        "fsp",
        10,
        1.1,
        11
    };
    print_receipt(&fsp);

    union test un = { 100 };
    printf("%d ## %c\n", un.a, un.c[0]);
}
