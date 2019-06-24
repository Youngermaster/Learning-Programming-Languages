/*
*	Quinto problema de condicionales con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que lea un caracter y diga si es mayuscula y minuscula.
*
*/

#include<iostream>

using namespace std;

int main(){
	
	char letra;
	
	cout<<"Septimo problema de condicionales con ATS"<<endl;
	cout<<"Este programa tiene la funcion de leer un caracter\ny decir si es vocal minuscula o mayuscula."<<endl;
	
	cout<<"\nDigite la letra"; cin>>letra;
	
	switch(letra){
		case 'a' :
		case 'e' :
		case 'i' :
		case 'o' :
		case 'u' : cout<<"\n\tEs una vocal minuscula";
		default : cout<<"\n\tNo es una vocal minuscula";
	}
	
	return 0;
}
