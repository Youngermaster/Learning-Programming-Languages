/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Cadena de caarcteres.
*
*/

#include <iostream>
#include <conio.h>
#include <string.h>

using namespace std;

int main()
{

	char nombre[] = "Juan";
	char nombre2[] = {'J', 'u', 'a', 'n'};
	char nombreCompleto[20];

	cout << "Digite un nombre: ";
	cin.getline(nombreCompleto, 20, '\n');

	cout << "\n"
		 << nombreCompleto << endl;

	getch();
	return 0;
}
