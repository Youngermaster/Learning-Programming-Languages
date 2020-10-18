/*
*	Primer problema de condicionales con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que lea dos numeros y determine cual de ellos es el mayor.
*
*/

#include <iostream>

using namespace std;

int main()
{

	int a, b;

	cout << "Primer problema de condicionales con ATS" << endl;
	cout << "El programa tiene la funcion de leer dos numeros y determine cual de ellos es el mayor." << endl;

	cout << "Digite el primer numero: " << endl;
	cin >> a;
	cout << "Digite el segundo numero: " << endl;
	cin >> b;

	a > b ? cout << "\n\tEl primer numero es mayor" : cout << "\n\tEl segundo numero es mayor";

	return 0;
}
