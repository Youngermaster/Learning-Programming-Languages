/*
*	Cadena de caracteres con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Comparar el contenido de dos cadenas.
*
*/

#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main(){
	
	char palabra1[] = "Prueba 1";
	char palabra2[] = "Prueba 1";
	
	if(strcmp(palabra1, palabra2)== 0){
		cout<<"Las dos cadenas son iguales."<<endl;
	}else{
		cout<<"Las dos cadenas son diferentes."<<endl;
	}
	
	system("pause");
	return 0;
}
