package main

import "fmt"

type User interface {
	Permissions() int
	Name() string
}

type Admin struct {
	name string
}

func (admin Admin) Permissions() int {
	return 5
}

func (admin Admin) Name() string {
	return admin.name
}

type Editor struct {
	name string
}

func (editor Editor) Permissions() int {
	return 3
}

func (editor Editor) Name() string {
	return editor.name
}

func auth(user User) string {
	permissionLevel := user.Permissions()
	if permissionLevel > 4 {
		return "The user has access."
	} else if permissionLevel == 3 {
		return "You have editor access"
	}
	return "You don't have access"
}

func main() {
	users := []User{Admin{"Lizeth"}, Editor{"Kasandra"}}
	for _, user := range users {
		fmt.Println(user.Name(), "->", auth(user))	
	}
}