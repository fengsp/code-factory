#include <iostream>

using namespace std;

int switch_magic(void) {
    static int i, state = 0;
    switch (state) {
        case 0:
        for (i = 0; i < 10; i++) {
            state = 1;
            return i;
            case 1:;
        }
    }

    return -1;
}

int main() {
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    cout << switch_magic() << endl;
    return 0;
}

