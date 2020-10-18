/*
*	Ordenamiento con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Bubble Sort.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

	int numeros[] = {4, 1, 2, 3, 5};
	int i, j, aux;

	cout << "Sin ordenar: " << endl;
	for (i = 0; i < 5; i++)
	{
		cout << numeros[i] << " ";
	}
	cout << endl;

	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			if (numeros[j] > numeros[j + 1])
			{
				aux = numeros[j];
				numeros[j] = numeros[j + 1];
				numeros[j + 1] = aux;
			}
		}
	}

	cout << "Ascendente: " << endl;
	for (i = 0; i < 5; i++)
	{
		cout << numeros[i] << " ";
	}
	cout << endl;

	cout << "Descendente: " << endl;
	for (i = 4; i >= 0; i--)
	{
		cout << numeros[i] << " ";
	}
	cout << endl;

	system("pause");
	return 0;
}
