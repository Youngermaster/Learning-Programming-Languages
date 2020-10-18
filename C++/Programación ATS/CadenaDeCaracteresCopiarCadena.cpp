/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Copiar el contenido de una cadena.
*
*/

#include <iostream>
#include <conio.h>
#include <string.h>

using namespace std;

int main()
{

	char nombre[] = "Juan";
	char nombre2[20];

	strcpy(nombre2, nombre);

	cout << "La cadena 1: " << nombre << endl;
	cout << "La cadena 2: " << nombre2 << endl;

	getch();
	return 0;
}
