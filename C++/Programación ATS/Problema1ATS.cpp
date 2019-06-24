/*
*	Primer Programa con ATS
*
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que lea de la entrada estandar dos numeros y muestre 
*	en la salida estandar su suma, su resta, su multiplicacion y su division.
*/

#include<iostream>

using namespace std;

int main(){
	
	int numero1, numero2, suma, resta, multiplicacion, division;
	
	cout<<"Por favor ingrese un numero\n";
	
	cin>>numero1;
	
	cout<<"Por favor ingrese otro numero\n";
	
	cin>>numero2;
	
	suma = numero1 + numero2;
	
	resta = numero1 - numero2;
	
	multiplicacion = numero1 * numero2;
	
	division = numero1 / numero2;
	
	cout<<"\nLa suma es: "<<suma;
	
	cout<<"\nLa resta es: "<<resta;
	
	cout<<"\nLa multiplicacion es: "<<multiplicacion;
	
	cout<<"\nLa division es: "<<division;
	
	cout<<"\nY eso es todo";
	
	return 0;
}
