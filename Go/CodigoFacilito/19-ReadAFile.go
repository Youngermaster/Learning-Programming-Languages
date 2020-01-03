package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	fileData, err := ioutil.ReadFile("assets/file.txt")

	if err != nil {
		fmt.Println("There was an error!")
	}

	fmt.Println(string(fileData))
}
