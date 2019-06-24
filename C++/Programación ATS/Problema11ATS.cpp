/*
*	Onceavo programa con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Escriba un programa que lea la nota alumnos video 9.
*
*/

#include<iostream>

using namespace std;

int main(){
	
	float notaPracticas, notaTeorica, notaParticipacion, total;
	
	cout<<"Onceavo programa de ATS";
	cout<<"\nEscriba un programa que lea la nota alumnos video 9."<<endl;
	
	cout<<"\nDigite la nota de practicas: "; cin>>notaPracticas;
	cout<<"\nDigite la nota teorica: "; cin>>notaTeorica;
	cout<<"\nDigite ka nota de participacion: "; cin>>notaParticipacion;
	
	total = (notaPracticas * 30 / 100) + (notaTeorica * 60 / 100) + (notaParticipacion * 10 / 100);
	
	cout<<"\n\tTu nota total es: "<<total;
	
	return 0;
}
