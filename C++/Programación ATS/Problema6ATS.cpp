/*
*	Sexto programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escribir la siguiente expresion en C++: A mas B, sobre C mas D.
*
*/

#include <iostream>

using namespace std;

int main()
{

	float A, B, C, D, total;

	cout << "Sexto programa ATS\n"
		 << endl;
	cout << "Este programa tiene la funcion de mostrar el resultado de A mas B, sobre C mas D\n"
		 << endl;

	cout << "Digite el numero A por favor: ";
	cin >> A;
	cout << "\nDigite el numero B por favor: ";
	cin >> B;
	cout << "\nDigite el numero C por favor: ";
	cin >> C;
	cout << "\nDigite el numero D por favor: ";
	cin >> D;

	total = (A + B) / (C + D);

	cout << "\n\tEl resultado es: " << total << endl;
	cout.precision(2);
	cout << "\n\tEl resultado redondeado es: " << total << endl;

	return 0;
}
