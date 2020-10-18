/*
*	Estructuras con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Estructura Basica.
*
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

struct persona
{
	char nombre[20];
	int edad;
} persona1 = {"Juan", 17},
  persona2 = {"Pedro Coco", 47},
  persona3;

int main()
{

	cout << "El nombre de la persona es: " << persona1.nombre << endl
		 << "Su edad es: " << persona1.edad << endl;
	cout << "El nombre de la persona es: " << persona2.nombre << endl
		 << "Su edad es: " << persona2.edad << endl;
	cout << endl
		 << "El nombre es: ";
	cin.getline(persona3.nombre, 20, '\n');
	cout << endl
		 << "La edad es: ";
	cin >> persona3.edad;

	cout << endl
		 << "El nombre de la persona es: " << persona3.nombre << endl
		 << "Su edad es: " << persona3.edad << endl;

	system("pause");
	return 0;
}
