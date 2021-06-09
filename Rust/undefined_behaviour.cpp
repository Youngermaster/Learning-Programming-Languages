#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Demo of Undefined Behaviour - dangling reference" << endl;
    cout << "-------------------------------------------------" << endl;

    vector<int> v;
    v.reserve(3);

    cout << "Capacity of v = " << v.size() << endl;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    
    for (auto &&i : v)
    {
        cout << i;
    }
    
    int& r1 = v[1];

    cout << "\n Address of V[1] = " << &v[1] << endl;
    cout << "Address of r1 = " << &r1 << endl;
    cout << "Value of r1 = " << r1 << endl;

    v.push_back(4);
    cout << "Push back caused reallocation" << endl;

    for (auto &&i : v)
    {
        cout << i;
    }

    cout << "\n Address of V[1] = " << &v[1] << endl;
    cout << "Address of r1 = " << &r1 << endl;
    cout << "Value of r1 = " << r1 << endl;


    return 0;
}
