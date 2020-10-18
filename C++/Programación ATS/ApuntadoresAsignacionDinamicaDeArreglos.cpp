/*
*	Apuntadores con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Pedir al usuario n calificaciones y almacenarlas en un arreglo dinamico.
*
*	Punteros.
*	&n = La direccion de n.
*	*n = La variable cuya direccion esta almacenada en n.
*
*	Asignacion dinamica de arreglos.
*
*	new: Reserva el numero de bytes solicitado por la declaracion.
*	delete: Libera un bloque de bytes reservado con anterioridad.
*
*/

#include <iostream>
#include <stdlib.h> // Funciona new y delete.
using namespace std;

// Prototipo de la funcion.
void PedirNotas();
void MostrarNotas();

int numCalif, *calif;

int main()
{

	PedirNotas();
	MostrarNotas();

	delete[] calif; // Liberando el espacio de bytes utilizados anteriormente.

	system("pause");
	return 0;
}

void PedirNotas()
{
	cout << "Digite el numero de calificaciones: ";
	cin >> numCalif;
	cout << endl;

	calif = new int[numCalif]; // Crea el arreglo.

	for (int y = 0; y < numCalif; y++)
	{
		cout << "Digita la nota: ";
		cin >> calif[y];
		cout << endl;
	}
}

void MostrarNotas()
{

	cout << "\nMostrando notas del usuario.\n"
		 << endl;
	for (int y = 0; y < numCalif; y++)
	{
		cout << "Nota " << y + 1 << ": " << calif[y] << endl;
	}
}
