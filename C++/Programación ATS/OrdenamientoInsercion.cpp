/*
*	Ordenamiento con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Insertion Sort.
*
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

int main(){
	
	int numeros[] = {4, 1, 2, 3, 5};
	int i, pos, aux;
	
	cout<<"Sin ordenar: "<<endl;
	for(i = 0 ; i < 5 ; i++){
		cout<<numeros[i]<<" ";
	}
	cout<<endl;

	for(i = 0 ; i < 5 ; i++){
		
		pos = i;
		aux = numeros[i];
		
		while((pos > 0) && (numeros[pos - 1] > aux)){
			numeros[pos] = numeros[pos - 1];
			pos--;
		}
		numeros[pos] = aux;
	}

	cout<<"Ascendente: "<<endl;
	for(i = 0 ; i < 5 ; i++){
		cout<<numeros[i]<<" ";
	}
	cout<<endl;
	
	cout<<"Descendente: "<<endl;
	for(i = 4 ; i >= 0 ; i--){
		cout<<numeros[i]<<" ";
	}
	cout<<endl;

	system("pause");
	return 0;
}
