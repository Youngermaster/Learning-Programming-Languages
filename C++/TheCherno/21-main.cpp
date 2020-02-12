#include <iostream>

#define LOG(x) std::cout << x << std::endl

int s_variable = 5;

// * To avoid the linking error we add extern
// * to get this variable from another file.
extern int noStaticVariable;

void function()
{
    LOG(s_variable);
    LOG(noStaticVariable);
}

int main(int argc, char const *argv[])
{
    function();
}
