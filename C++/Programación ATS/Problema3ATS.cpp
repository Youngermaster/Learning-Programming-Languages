/*
*	Tercer programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Realiceun programa que lea de la entrada estandar los siguientes datos de una persona:
*	
*	Edad: Tipo entero
*	Sexo: Tipo char
*	Altura: Tipo real
*
*	Tras leer los datos, el programa debe mostrarlos en la salida de datos estandar.
*/

#include<iostream>

using namespace std;

int main(){
	
	int edad;
	char sexo[10];
	float altura;
	
	cout<<"Tercer programa ATS\n"<<endl;
	cout<<"Este programa tiene la funcion de mostrar los datos anteriormente digitados\n"<<endl;
	
	cout<<"Digite la edad por favor: "; cin>>edad;
	cout<<"\nDigite el genero por favor: "; cin>>sexo;
	cout<<"\nDigite la altura por favor: "; cin>>altura;
	
	cout<<"\n\tEdad: "<<edad<<endl;
	cout<<"\n\tSexo: "<<sexo<<endl;
	cout<<"\n\tAltura en metros: "<<altura<<endl;
	
	return 0;
}
