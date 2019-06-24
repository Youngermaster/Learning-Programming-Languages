/*
*	Pilas con ATS
*		
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que haga lo siguiente:
*
*	Insertar elementos en una pila.
*
*	LIFO Last Input First Output.
*	El ultimo en entrar ee el primero en salir.
*	
*/

#include<iostream>
#include<stdlib.h> // Sirve para el new.
using namespace std;

struct Nodo{
	int dato;
	Nodo *siguiente;
};

// Prototipo de la funcion.
void agregarPila(Nodo *&, int);

int main(){
	int n1, n2;
	Nodo *pila = NULL;	
	cout<<"Digite un numero: "; cin>>n1;
	agregarPila(pila, n1);
	
	cout<<"Digite otro numero: "; cin>>n2;
	agregarPila(pila, n2);
	
	system("pause");
	return 0;
}

void agregarPila(Nodo *&pila, int n){
	Nodo *nuevo_nodo = new Nodo();
	nuevo_nodo -> dato = n;
	nuevo_nodo -> siguiente = pila;
	pila = nuevo_nodo;
	
	cout<<endl<<"Numero "<<n<<" agregado correctamente."<<endl;
}
