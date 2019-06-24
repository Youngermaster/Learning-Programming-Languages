/*
*	Noveno programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un fragmento de programa que intercambie los valores de dos variables.
*
*/

#include<iostream>

using namespace std;

int main(){
	
	float x, y, aux;
	
	cout<<"Noveno programa ATS\n"<<endl;
	cout<<"Este programa tiene la funcion de intercambiar los valores de dos variables\n"<<endl;
	
	cout<<"\nDigite el primer valor: "; cin>>x;
	cout<<"\nDigite el segundo valor: "; cin>>y;
	
	aux = x;
	x = y;
	y = aux;
	
	cout<<"\n\tEl nuevo valor del primer numero es: "<<x;
	cout<<"\n\tEl nuevo valor del segundo numero es: "<<y;
	
	
	return 0;
}
