/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Convertir a Mayuscula el contenido de una cadena.
*
*/

#include<iostream>
#include<stdlib.h>
#include<string.h>

using  namespace std;

int main(){
	
	char nombre[] = "Juan Manuel Young Hoyos";
	
	cout<<"Nombre sin mayusculas: "<<nombre<<endl<<endl;
	
	strupr(nombre);
	
	cout<<"Nombre con Mayusculas: "<<nombre<<endl<<endl;
	
	system("pause");
	return 0;
}
