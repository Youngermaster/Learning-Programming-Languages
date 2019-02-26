#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int number;
    int data = 5;

    cout<< "Enter a number: ";
    cin>> number;
    if (number == 5)
    {
        cout<<endl<< "The number is 5"<<endl;
    } else if (number > 5)
    {
        cout<<endl<< "The number if bigger than 5"<<endl;
    } else if (number < 5)
    {
        cout<<endl<< "The number is smaller than 5"<<endl;
    }
    return 0;
}
