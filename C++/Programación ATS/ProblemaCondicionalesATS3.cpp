/*
*	Segundo problema de condicionales con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que lea un numero y determine si es par o impar.
*
*/

#include <iostream>

using namespace std;

int main()
{

	int numero;

	cout << "Segundo problema de condicionales con ATS" << endl;
	cout << "El programa tiene la funcion de leer un numero y determinar si es par o impar." << endl;

	cout << "Digite el numero: ";
	cin >> numero;

	numero % 2 == 0 && numero != 0 ? cout << "\n\tEl numero es par." : numero == 0 ? cout << "\n\tEl numero es cero (0)." : cout << "\n\tEl numero es impar.";

	return 0;
}
