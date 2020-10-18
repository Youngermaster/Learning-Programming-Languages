/*
*	Apuntadores con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Intercambiar el valor de dos numeros.
*
*	Transmision de direcciones.
*
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

// Prototipo
void intercambio(float *, float *);

int main()
{
	float num1, num2;

	cout << "Digite el primer Numero: ";
	cin >> num1;
	cout << endl
		 << "Digite el segundo Numero:";
	cin >> num2;

	cout << endl
		 << endl
		 << "Antes del intercambio." << endl;
	cout << endl
		 << "\tEl numero 1 es: " << num1;
	cout << endl
		 << "\tEl numero 2 es: " << num2;

	intercambio(&num1, &num2);

	cout << endl
		 << endl
		 << "Despues del intercambio." << endl;
	cout << endl
		 << "\tEl numero 1 es: " << num1;
	cout << endl
		 << "\tEl numero 2 es: " << num2 << endl;

	system("pause");
	return 0;
}

void intercambio(float *dir_num1, float *dir_num2)
{
	float aux;

	aux = *dir_num1;
	*dir_num1 = *dir_num2;
	*dir_num2 = aux;
}
