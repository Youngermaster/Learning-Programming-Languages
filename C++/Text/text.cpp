#include <iostream>
#include <Windows.h>

using namespace std;

int main()
{
	HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(handle, FOREGROUND_RED | FOREGROUND_INTENSITY); // Set the text red.
	cout << "Red Text" << endl;
	SetConsoleTextAttribute(handle, FOREGROUND_BLUE | FOREGROUND_INTENSITY);

	for (int i = 0; i < 10; i += 2)
		cout << "Line number: " << i << endl;

	system("pause");
	return 0;
}