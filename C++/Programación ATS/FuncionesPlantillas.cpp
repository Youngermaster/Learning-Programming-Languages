/*
*	Plantillas de Funciones con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Sacar el valor absoluto de un numero.
*
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

// Prototipo de funcion.
template <class TIPOD>
void showAbsolute(TIPOD number);

int main(){
	
	int n1 = 41;
	float n2 = -2312;
	double n3 = -3134;
	
	showAbsolute(n1);
	showAbsolute(n2);
	showAbsolute(n3);
	
	system("pause");
	return 0;
}

template <class TIPOD>
void showAbsolute(TIPOD number){
	number < 0 ? number *= -1 : number;
	cout<<"El valor absoluto de un numero es: "<<number<<endl;
}
