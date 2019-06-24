/*
*	Estructuras con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Estructura anidadas.
*
*/

#include<iostream>
#include<stdlib.h>

using namespace std;

struct info_direccion{
	char direccion[30];
	char ciudad[20];
	char provincia[20];	
};

struct empleado{
	char nombre[20];
	struct info_direccion dir_empleado;
	double salario;
}empleados[2];

int main(){
	
	// Recolectando los datos del usuario.
	for(int y = 0 ; y < 2 ; y++){
		fflush(stdin);
		
		cout<<"Digite el nombre de su empleado: ";
		cin.getline(empleados[y].nombre, 20, '\n');
		
		fflush(stdin);
		
		cout<<endl<<"Digite el salario: ";
		cin>>empleados[y].salario;
		
		fflush(stdin); // Vacia el buffer y permitir digitar los valores.
		
		cout<<endl<<"Digite la provincia: ";
		cin.getline(empleados[y].dir_empleado.provincia, 20, '\n');
		
		fflush(stdin);
		
		cout<<endl<<"Digite la ciudad: ";
		cin.getline(empleados[y].dir_empleado.ciudad, 20, '\n');
		
		fflush(stdin);
		
		cout<<endl<<"Digite la direccion: ";
		cin.getline(empleados[y].dir_empleado.direccion, 30, '\n');
		
		cout<<endl;
	}
	
	// Imprimiendo los datos del usuario.
	
	for(int x = 0 ; x < 2 ; x++){
		cout<<"Datos del Empleado "<<x + 1<<": "<<endl;
		cout<<"Nombre: "<<empleados[x].nombre<<endl;
		cout<<"Salario: "<<empleados[x].salario<<endl;
		cout<<"Provincia: "<<empleados[x].dir_empleado.provincia<<endl;
		cout<<"Ciudad: "<<empleados[x].dir_empleado.ciudad<<endl;
		cout<<"Direccion: "<<empleados[x].dir_empleado.direccion<<endl<<endl;
	}
	
	system("pause");
	return 0;
}

