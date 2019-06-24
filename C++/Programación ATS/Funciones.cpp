/*
*	Funciones con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Encontrar el mayor de dos numeros enteros.
*
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

// Declarar funciones.

int numeroMax(int x, int y);

int main(){
	
	int n1, n2;
	
	cout<<"Digite dos numeros."<<endl;
	cout<<endl<<"Digite el primer numero: "; cin>>n1;
	cout<<endl<<"Digite el segundo numero: "; cin>>n2;
	
	cout<<endl<<endl<<"\tEl numero mayor es: "<<numeroMax(n1, n2)<<endl;
	
	system("pause");
	return 0;
}

// Definicion de funciones.

int numeroMax(int x, int y){
	return x > y? x : y;
}
