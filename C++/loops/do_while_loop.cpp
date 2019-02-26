#include <iostream>

using namespace std;
int main(int argc, char const *argv[])
{
    int iterator;
    iterator = 0;

    do
    {
        cout<<"iterator = "<<iterator<<endl;
        iterator++;
    } while (iterator <= 10);
    
    return 0;
}
