/*
*	Quinto programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escribir la siguiente expresion en C++: A sobre B mas 1
*
*/

#include<iostream>

using namespace std;

int main(){
	
	float A, B, C;
	
	cout<<"Quinto programa ATS\n"<<endl;
	cout<<"Este programa tiene la funcion de mostrar el resultado de A sobre B mas el numero 1\n"<<endl;
	
	
	cout<<"Digite el numero A por favor: "; cin>>A;
	cout<<"\nDigite el numero B por favor: "; cin>>B;
	
	C = (A / B) + 1;
	
	cout<<"\n\tEl resultado es: "<<C<<endl;
	cout.precision(2);
	cout<<"\n\tEl resultado redondeado es: "<<C<<endl;
	
	return 0;
}

