#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Demo of Undefined Behaviour - out of bounds index" << endl;
    cout << "-------------------------------------------------" << endl;

    int array[3]{1, 2, 3};

    for (int i = 0; i <= 3; i++)
    {
        cout << array[i] << " ";
    }

    // ! How to avoid the Undefined Behavior
    cout << endl;
    for (auto i : array)
    {
        cout << i << " ";
    }
    
    return 0;
}
