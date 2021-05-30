#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;

int main()
{
    time_t t = time(NULL);
    tm *tPtr = localtime(&t);
    cout << "\n\n Display the Current Date and Time :\n";
    cout << "----------------------------------------\n";
    cout << " seconds = " << (tPtr->tm_sec) << endl;
    cout << " minutes = " << (tPtr->tm_min) << endl;
    cout << " hours = " << (tPtr->tm_hour) << endl;
    cout << " day of month = " << (tPtr->tm_mday) << endl;
    cout << " month of year = " << (tPtr->tm_mon) + 1 << endl;
    cout << " year = " << (tPtr->tm_year) + 1900 << endl;
    cout << " weekday = " << (tPtr->tm_wday) << endl;
    cout << " day of year = " << (tPtr->tm_yday) << endl;
    cout << " daylight savings = " << (tPtr->tm_isdst) << endl;
    cout << endl;
    cout << endl;

    cout << " Current Date: " << (tPtr->tm_mday) << "/" << (tPtr->tm_mon) + 1 << "/" << (tPtr->tm_year) + 1900 << endl;
    cout << " Current Time: " << (tPtr->tm_hour) << ":" << (tPtr->tm_min) << ":" << (tPtr->tm_sec) << endl;
    cout << endl;
    return 0;
}
