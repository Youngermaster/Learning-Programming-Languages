#include <iostream>

int main() {
    using namespace std;
    int x = 10;
    cout << "&x -> " << &x << "\n";
    //int *ptr = nullptr;
    int* ptr = &x;
    cout << "*ptr -> " << *ptr << "\n";
    cout << "ptr -> " << ptr << endl;

    cout << "------------------------" << endl;

    int y = 50;
    ptr = &y;
    cout << "&x -> " << &x << "\n";
    cout << "x -> " << x << "\n";
    cout << "&y -> " << &y << "\n";
    cout << "y -> " << y << "\n";

    cout << "*ptr -> " << *ptr << "\n";
    cout << "ptr -> " << ptr << endl;

    return 0;
}