#include <iostream>
#include <Windows.h>

using namespace std;

int intSum(int, int);
void welcomeMessage();
void startNewProgram(string);

int main()
{
	int x;
	int y;

	welcomeMessage();

	cout << "Enter X value: ";
	cin >> x;
	cout << endl << "Enter Y Value: ";
	cin >> y;

	cout << "The sum is: " << intSum(x, y) << endl;
	cout << "Opening paint..."
	startNewProgram("mspaint");
	system("pause");
	return 0;
}

int intSum(int x, int y)
{
	cout << "Executing the sum..." << endl;
	return x + y;
}

void welcomeMessage()
{
	cout << "Hello, welcome to ur program!" << endl;
}

void startNewProgram(string fileName)
{
	ShellExecute(NULL, "open", fileName.c_str(), NULL, NULL, SW_SHOWNORMAL);
}