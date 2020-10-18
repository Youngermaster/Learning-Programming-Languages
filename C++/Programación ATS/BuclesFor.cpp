/*
*	Bucle o ciclos For con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que imprima los 11 primeros numeros impares.
*
*/

#include <iostream>
#include <conio.h>

using namespace std;

int main()
{

	cout << "For" << endl
		 << endl;

	for (int i = 0; i <= 10; i++)
	{
		cout << i + (i + 1) << endl;
	}

	getch(); // Lo mismo que el getch.
	return 0;
}
