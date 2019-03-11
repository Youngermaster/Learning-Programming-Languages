#include <iostream>
#include <iomanip> // ! The second way.

using namespace std;

int main(int argc, char const *argv[])
{
    // * This is one way.
    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(2);

    // * This is the second way.+
    cout << fixed << showpoint << setprecision(3);

    double input;

    cout << "Digit a number" << endl;
    cin>> input;

    cout << input;

    return 0;
}
