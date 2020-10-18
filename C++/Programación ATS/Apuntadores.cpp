/*
*	Apuntadores con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Punteros.
*	&n = La direccion de n.
*	*n = La variable cuya direccion esta almacenada en n.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
	int num = 20; // Variable común.
	int *dir_num; // Apuntador.

	dir_num = &num;

	cout << "Normalito" << endl;
	cout << "Numero: " << num << endl;
	cout << "Direccion: " << &num << endl;

	cout << endl
		 << "De otra manera" << endl;
	cout << "Numero: " << *dir_num << endl;	  // Con el asterisco es igual a la variable.
	cout << "Direccion: " << dir_num << endl; // Igual a la direccion de la variable en hexadecimal.

	system("pause");
	return 0;
}
