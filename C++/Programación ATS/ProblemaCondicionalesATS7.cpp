/*
*	Septimo problema de condicionales con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que reciba una edad y diga que si esta en el rango [18-25].
*
*/

#include <iostream>

using namespace std;

int main()
{

	int edad

			cout
		<< "Septimo problema de condicionales con ATS" << endl;
	cout << "Este programa tiene la funcion de recibir una edad\ny decir si esta en el rango de 18 a 25." << endl;

	cout << "\nDigite su edad por favor.";
	cin >> edad;

	edad >= 18 && edad <= 25 ? cout << "\n\tSu edad esta en el rango" : cout << "\ntSu edad no esta en el rango";

	return 0;
}
