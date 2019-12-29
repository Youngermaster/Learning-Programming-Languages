package main

import "fmt"

func main() {
	newTeacher := Teacher{Human{"Shanny"}, Dummy{"Theodore"}}
	// fmt.Println(newTeacher.name) // ! ambiguous selector newTeacher.name
	fmt.Println(newTeacher.Human.name)
	fmt.Println(newTeacher.Dummy.name)
	
	fmt.Println(newTeacher.speak())
	fmt.Println(newTeacher.Human.speak())
}

type Human struct {
	name string
}

func (human Human) speak() string {
	return "Bla bla bla"
}

type Dummy struct {
	name string
}

type Teacher struct {
	Human
	Dummy
}

func (teacher Teacher) speak() string {
	return "I'am a teacher"
}


