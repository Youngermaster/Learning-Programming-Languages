#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    // The sum of the array
    int numbers[] = {1, 2, 3, 4, 5};
    int sum;
    sum = 0;

    for(int i = 0; i < 5; i++)
        sum += numbers[i];

    cout << "The sum of the array is: "<< sum << endl;
    
    return 0;
}
