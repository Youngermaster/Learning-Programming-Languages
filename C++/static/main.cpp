#include <iostream>

extern int g_variable;

void function()
{
    // stuff
}

struct Entity
{
    int x, y;
    static int s_x, s_y;

    void print()
    {
        std::cout << x << ", " << y << std::endl;
    }
};

int main(int argc, char const *argv[])
{
    std::cout << g_variable << std::endl;

    Entity e1;
    e1.x = 1;
    e1.y = 2;

    Entity e2 = {6, 7};



    return 0;
}
