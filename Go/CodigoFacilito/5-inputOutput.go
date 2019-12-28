package main

import (
	"os"
	"fmt"
	"bufio"
)

func main() {
	// * fmt  way
	
	/*
	* Prints
	*/
	fmt.Println("=========== Prints ===========")
	age := 22
	fmt.Printf("My age is %d.\n", age)

	// * 'v' flag support the necessary data type.
	// * 
	vFlag := 18
	fmt.Printf("My age is %v.\n", vFlag)


	name := "Juan"
	fmt.Printf("Hello %s.\n", name)

	boolean := false
	fmt.Printf("The sky is red: %t.\n", boolean)

	price := 19.99
	fmt.Printf("The price is: %f.\n", price)
	fmt.Printf("The price is: %e.\n", price)
	fmt.Printf("The price is: %b.\n", price)

	/*
	* Scans
	*/

	fmt.Println("=========== Scans ===========")
	var yourAge int
	fmt.Println("Write your age: ")
	fmt.Scanf("%d\n", &yourAge)
	fmt.Printf("Your age is: %d.\n", yourAge)


	// * bufio way
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("write your name: ")
	yourName, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("Your name is: %s.\n", yourName)
	}
	

}