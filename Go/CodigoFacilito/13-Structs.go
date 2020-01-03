package main

import "fmt"

type user struct {
	name     string
	lastName string
	age      int
}

func main() {
	rollin := user{name: "Rollin", lastName: "Fadel", age: 98705}
	uriel := user{"Uriel", "Hernández", 20}
	christy := new(user) // * Get the memory address.
	*christy = user{name: "Christy", lastName: "Dare"}
	(*christy).age = 19

	fmt.Println(rollin)
	fmt.Println(uriel)
	fmt.Println((*christy).name) // * It's exactly to the last one Print.
	fmt.Println(christy.age)
}
