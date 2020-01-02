#include <iostream>

#define LOG(x) std::cout << x << std::endl

struct Entity
{
    int x, y;
    void Print() {
        std::cout << "X: " << x << " Y: " << y << std::endl;
    }
};

struct Entity2
{
    static int x, y;
    void Print() {
        std::cout << "X: " << x << " Y: " << y << std::endl;
    }
    // ! if we want to use static functions the variables
    // ! that we use should be static too.
    static void s_Print() {
        std::cout << "X: " << x << " Y: " << y << std::endl;
    }
};

int Entity2::x;
int Entity2::y;

int main(int argc, char const *argv[])
{
    Entity e;
    e.x = 10;
    e.y = 12;

    Entity e1 = {1, 2};
    e.Print();
    e1.Print();

    // ! We can't use `{}` to instaciate a struct.
    Entity2 e2;
    e2.x = 10;
    e2.y = 12;

    // * Instead of e21.x = 1; you can use:
    Entity2 e21;
    Entity2::x = 1;
    Entity2::y = 2;
    // * You can use that code because the static variables
    // * are shared by all the instances.

    e2.Print();
    e21.Print();

    return 0;
}
