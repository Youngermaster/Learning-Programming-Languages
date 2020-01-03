package main

import "fmt"

type user interface {
	Permissions() int
	Name() string
}

type admin struct {
	name string
}

func (admin admin) Permissions() int {
	return 5
}

func (admin admin) Name() string {
	return admin.name
}

type editor struct {
	name string
}

func (editor editor) Permissions() int {
	return 3
}

func (editor editor) Name() string {
	return editor.name
}

func auth(user user) string {
	permissionLevel := user.Permissions()
	if permissionLevel > 4 {
		return "The user has access."
	} else if permissionLevel == 3 {
		return "You have editor access"
	}
	return "You don't have access"
}

func main() {
	users := []user{admin{"Lizeth"}, editor{"Kasandra"}}
	for _, user := range users {
		fmt.Println(user.Name(), "->", auth(user))
	}
}
