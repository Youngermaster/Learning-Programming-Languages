/*
*	Apuntadores con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Hallar el maximo elemento de un arreglo.
*
*	Transmision de arreglos.
*
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

// Prototipo de funcion.
int hallarMax(int *, int);

int main()
{

	const int nElementos = 5;
	int numeros[nElementos] = {1, 2, 34, 6, 8};

	cout << "El mayor numero es: " << hallarMax(numeros, nElementos) << endl;

	system("pause");
	return 0;
}

int hallarMax(int *dirVec, int nElementos)
{
	int max = 0;

	for (int y = 0; y < nElementos; y++)
	{
		if (*(dirVec + y) > max)
		{
			max = *(dirVec + y);
		}
	}
	return max;
}
