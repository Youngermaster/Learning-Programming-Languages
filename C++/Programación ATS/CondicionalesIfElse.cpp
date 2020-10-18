/*
*	Estrucutra if else programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Sentencia If Else.
*
*/

#include <iostream>

using namespace std;

int main()
{

	int numero;

	cout << "\nDigite un numero: ";
	cin >> numero;

	if (numero % 2 == 0 || numero == 0)
	{
		cout << "\nEl numero es par o es cero (0).";
	}
	else
	{
		cout << "\nEl numero es impar.";
	}

	return 0;
}
