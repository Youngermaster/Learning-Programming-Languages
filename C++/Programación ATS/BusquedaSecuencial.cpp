/*
*	Busquedas en arreglos con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Busqueda secuencial.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

	int numeros[] = {1, 2, 3, 4, 5};
	int i, dato;
	char bandera = 'F';

	dato = 5;

	i = 0;
	while ((bandera == 'F') && (i < 5))
	{
		if (numeros[i] == dato)
		{
			bandera = 'T';
		}
		i++;
	}

	bandera == 'F' ? cout << "El numero no existe en el arreglo" << endl : cout << "El numero ha sido encontrado en la posicion: " << i - 1 << endl;

	system("pause");
	return 0;
}
