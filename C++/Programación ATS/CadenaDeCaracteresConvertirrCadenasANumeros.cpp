/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Convertir a minuscula el contenido de una cadena.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

	char numero1[] = "117";
	char numero2[] = "7.11";

	int num1;
	float num2;

	num1 = atoi(numero1); // Enteros
	num2 = atof(numero2); // Flotantes

	cout << "Numero 1: " << num1 << endl;
	cout << "Numero 2: " << num2 << endl;
	cout << "\tSu suma es: " << (num1 + num2) << endl;

	system("pause");
	return 0;
}
