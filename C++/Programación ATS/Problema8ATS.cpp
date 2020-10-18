/*
*	Octavo programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escribir la siguiente expresion en C++: A mas B sobre C menos D.
*
*/

#include <iostream>

using namespace std;

int main()
{

	float A, B, C, D, resultado;

	cout << "Octavo programa ATS\n"
		 << endl;
	cout << "Este programa tiene la funcion de mostrar el resultado de A mas B sobre C menos D." << endl;

	cout << "\nDigite el numero A: ";
	cin >> A;
	cout << "\nDigite el numero B: ";
	cin >> B;
	cout << "\nDigite el numero C: ";
	cin >> C;
	cout << "\nDigite el numero D: ";
	cin >> D;

	resultado = A + (B / (C - D));

	cout << "\n\tEl resultado es: " << resultado;

	return 0;
}
