/*
*	Busquedas en arreglos con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Busqueda Binaria.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

	int number[] = {1, 2, 3, 4, 5};
	int bottom, top, middle, date;
	char flag = 'F';

	date = 3;
	bottom = 0;
	top = 5;

	while (bottom <= top)
	{
		middle = (bottom + top) / 2;
		if (number[middle] == date)
		{
			flag = 'T';
			break;
		}
		if (number[middle] > date)
		{
			top = middle;
			middle = (bottom + top) / 2;
		}
		if (number[middle] > date)
		{
			bottom = middle;
			middle = (bottom + top) / 2;
		}
	}

	flag == 'T' ? cout << "El numero ha sido encontrado en la posicion: " << middle << endl : cout << "El numero no ha sido encontrado." << endl;

	system("pause");
	return 0;
}
