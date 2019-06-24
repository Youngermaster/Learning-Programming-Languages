/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Longitud de cadena de caracteres.
*
*/

#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

int main(){
	
	char palabra[] = "Palabra";
	
	int longitud = strlen(palabra);
	
	cout<<"La cantidadde caracteres que tiene 'Palabra' es: "<<longitud;
	
	getch();
	return 0;
}
