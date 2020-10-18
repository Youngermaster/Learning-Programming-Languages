/*
*	Treceavo programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que video 10.
*
*/

#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	float x, y, resultado;

	cout << "\nTreceavo programa de ATS";
	cout << "\nVideo 10" << endl;

	cout << "\nDigita el valor de \"X\": ";
	cin >> x;
	cout << "\nDigita el valor de \"Y\": ";
	cin >> y;

	resultado = (sqrt(x)) / ((pow(y, 2)) - 1);

	cout << "\n\tEl resultado es: " << resultado;

	return 0;
}
