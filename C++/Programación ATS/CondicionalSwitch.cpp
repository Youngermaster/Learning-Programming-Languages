/*
*	Estrucutra switch programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Sentencia switch.
*
*/

#include <iostream>

using namespace std;

int main()
{

	int numero;
	cout << "Digita un numero entre el 1 y el 5: ";
	cin >> numero;

case (numero) {
	case 1:
	cout << "El numero es 1";
	break;
case 2:
	cout << "El numero es 2";
	break;
case 3:
	cout << "El numero es 3";
	break;
case 4:
	cout << "El numero es 4";
	break;
case 5:
	cout << "El numero es 5";
	break;
default:
	cout << "El numero no esta en el rango de 1 y 5";
	break;
}

return 0;
}
