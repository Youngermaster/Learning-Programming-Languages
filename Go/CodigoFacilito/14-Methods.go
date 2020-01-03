package main

import "fmt"

type user struct {
	name     string
	lastName string
	age      int
}

func (user user) getFullName() string {
	return user.name + " " + user.lastName
}

func (user user) getAge() int {
	return user.age
}

func (user *user) setAge(age int) {
	user.age = age
}

func main() {
	rollin := user{name: "Rollin", lastName: "Fadel", age: 4438}

	fmt.Println(rollin)

	rollin.setAge(29)

	fmt.Println(rollin.getFullName(), "Age is", rollin.getAge())
}
