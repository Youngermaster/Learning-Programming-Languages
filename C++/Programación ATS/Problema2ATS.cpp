/*
*	Segundo Problema
*
*	Juan Manuel Young Hoyos	
*
*	Escriba un programa que lea la entrada estandar de un producto y muestre la salida 
*	estandar del precio del producto al aplicarle el IVA.
*/

#include<iostream>

using namespace std;

int main(){
	
	double precioDelProducto, IVA, PrecioTotal;
	
	cout<<"Por favor digite el precio del producto."<<endl;
	
	cin>>precioDelProducto;
	
	IVA = (precioDelProducto *  19) / 100; // 19 porque es el precio IVA de Colombia
	
	PrecioTotal = precioDelProducto + IVA;
	
	cout<<"\nEl precio del producto con el IVA es: "<<PrecioTotal;
	
	return 0;
}
