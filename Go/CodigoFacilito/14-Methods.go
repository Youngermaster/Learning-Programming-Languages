package main

import "fmt"

type User struct {
	name string
	lastName string
	age int
}

func (user User) getFullName() string {
	return user.name + " " + user.lastName
}

func (user User) getAge() int {
	return user.age
}

func (user *User) setAge(age int) {
	user.age = age
}

func main() {
	rollin := User{name: "Rollin", lastName: "Fadel", age: 4438 }
	
	
	fmt.Println(rollin)

	rollin.setAge(29)
	
	fmt.Println(rollin.getFullName(), "Age is", rollin.getAge())
}