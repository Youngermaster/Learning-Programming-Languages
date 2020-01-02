#include <iostream>
#define LOG(x) std::cout << x << std::endl

// * Enums store a 4 bytes integers
// * In this case, if we left the code like that
// * the values will be start from zero
enum Level {
    zero, one, two, three
};

enum Abc : unsigned char {
    A = 'A',
    B = 'B',
    C = 'C'
};

int main(int argc, char const *argv[])
{
    LOG("Level enum");
    LOG(Level::zero);
    LOG("==================");
    LOG("Abc enum");
    LOG(Abc::B);
    return 0;
}
