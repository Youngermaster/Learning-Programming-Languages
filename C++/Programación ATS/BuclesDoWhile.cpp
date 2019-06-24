/*
*	Bucle o ciclos Do While con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que imprima los numeros del 10 al 1.
*
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

int main(){
	
	int i = 10;
	
	cout<<"Do While"<<endl<<endl;
	
	do{
		cout<<"El numero: "<<i<<endl;
		i--;
	}while(i > 0);
	
	system("pause"); // Lo mismo que el getch.
	return 0;
}
