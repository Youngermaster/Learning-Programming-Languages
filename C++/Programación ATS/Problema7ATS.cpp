/*
*	Septimo programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escribir la siguiente expresion en C++: A mas B sobre C, sobre D mas E sobre F.
*
*/

#include <iostream>

using namespace std;

int main()
{

	float A, B, C, D, E, F, Resultado;

	cout << "Septimo programa ATS\n"
		 << endl;
	cout << "Este programa tiene la funcion de mostrar el resultado de A mas B sobre C, sobre D mas E sobre F." << endl;

	cout << "\nDigite el numero A por favor: ";
	cin >> A;
	cout << "\nDigite el numero B por favor: ";
	cin >> B;
	cout << "\nDigite el numero C por favor: ";
	cin >> C;
	cout << "\nDigite el numero D por favor: ";
	cin >> D;
	cout << "\nDigite el numero E por favor: ";
	cin >> E;
	cout << "\nDigite el numero F por favor: ";
	cin >> F;

	Resultado = (A + (B / C)) / (D + (E / F));

	cout << "\n\tEl resultado es: " << Resultado;

	return 0;
}
