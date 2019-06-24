/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Concatenar el contenido de dos cadenas.
*
*/

#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main(){
	
	char cadena1[] = "Prueba1";
	char cadena2[] = " Prueba2";
	
	strcat(cadena1, cadena2);
	
	cout<<cadena1<<endl;
	
	system("pause");
	return 0;
}
