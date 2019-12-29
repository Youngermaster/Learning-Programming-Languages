package main

import "fmt"

type User struct {
	name string
	lastName string
	age int
}

func main() {
	rollin := User{name: "Rollin", lastName: "Fadel", age: 98705 }
	uriel := User{"Uriel", "Hernández", 20}
	christy := new(User) // * Get the memory address.
	*christy = User{name: "Christy", lastName: "Dare"}
	(*christy).age = 19

	fmt.Println(rollin)
	fmt.Println(uriel)
	fmt.Println((*christy).name) // * It's exactly to the last one Print.
	fmt.Println(christy.age)
}