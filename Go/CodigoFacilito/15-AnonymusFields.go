package main

import "fmt"

func main() {
	newteacher := teacher{human{"Shanny"}, dummy{"Theodore"}}
	// fmt.Println(newteacher.name) // ! ambiguous selector newteacher.name
	fmt.Println(newteacher.human.name)
	fmt.Println(newteacher.dummy.name)

	fmt.Println(newteacher.speak())
	fmt.Println(newteacher.human.speak())
}

type human struct {
	name string
}

func (human human) speak() string {
	return "Bla bla bla"
}

type dummy struct {
	name string
}

type teacher struct {
	human
	dummy
}

func (teacher teacher) speak() string {
	return "I'am a teacher"
}
