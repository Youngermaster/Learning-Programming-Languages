/*
*	Cuarto programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Ejecute el programa del problema anterior con entradas erroneas y observe los resultados.
*	Por ejemplo, introduzca un dato de tipo caracter cuando se espera un dato de tipo entero.
*	
*/

#include <iostream>

using namespace std;

int main()
{

	int edad;
	char sexo[10];
	float altura;

	cout << "Cuarto programa ATS\n"
		 << endl;
	cout << "Este programa tiene la funcion de mostrar los datos anteriormente digitados, pero de manera erronea\n"
		 << endl;

	cout << "Digite la edad por favor: ";
	cin >> edad;
	cout << "\nDigite el genero por favor: ";
	cin >> sexo;
	cout << "\nDigite la altura por favor: ";
	cin >> altura;

	cout << "\n\tEdad: " << edad << endl;
	cout << "\n\tSexo: " << sexo << endl;
	cout << "\n\tAltura en metros: " << altura << endl;

	return 0;
}
