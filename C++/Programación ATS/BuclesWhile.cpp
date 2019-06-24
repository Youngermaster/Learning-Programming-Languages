/*
*	Bucle o ciclos While con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que imprima los numeros del 1 al 10.
*
*/

#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	
	int i = 0;
	
	cout<<"While"<<endl<<endl;
	
	while(i <= 10){
		cout<<"El numero: "<<i<<endl;
		i++;
	}
	
	getch();
	return 0;
}


