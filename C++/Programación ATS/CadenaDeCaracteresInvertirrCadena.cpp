/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Invertir el contenido de dos cadenas.
*
*/

#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main(){
	
	char polindromas[] = "Anita la balatinA";
	char capicuas[] = "reconocer";
	
	cout<<"Palabra original: \n"<<polindromas<<endl<<capicuas<<endl<<endl;
	
	strrev(polindromas);
	strrev(capicuas);
	
	cout<<"Palabra invertida: \n"<<polindromas<<endl<<capicuas<<endl<<endl;
	
	system("pause");
	return 0;
}
