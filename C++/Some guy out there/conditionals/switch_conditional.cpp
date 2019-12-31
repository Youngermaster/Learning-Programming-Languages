#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int number;

    cout<< "Enter a number among 1 and 5: ";
    cin>> number;
    switch (number)
    {
        case 1:
            cout<<endl<< "The number is 1."<<endl;
            break;
        case 2:
            cout<<endl<< "The number is 2."<<endl;
            break;
        case 3:
            cout<<endl<< "The number is 3."<<endl;
            break;
        case 4:
            cout<<endl<< "The number is 4."<<endl;
            break;
        case 5:
            cout<<endl<< "The number is 5."<<endl;
            break;
        default:
            cout<<endl<< "It isn't in the range."<<endl;
            break;
    }
    return 0;
}
