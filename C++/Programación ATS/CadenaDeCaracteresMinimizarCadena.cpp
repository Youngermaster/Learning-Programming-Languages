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
#include <string.h>

using namespace std;

int main()
{

	char nombre[] = "Juan Manuel Young Hoyos";

	cout << "Nombre sin Minuscula: " << nombre << endl
		 << endl;

	strlwr(nombre);

	cout << "Nombre con minuscula: " << nombre << endl
		 << endl;

	system("pause");
	return 0;
}
