package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	file_data, err := ioutil.ReadFile("assets/file.txt")

	if err != nil {
		fmt.Println("There was an error!")
	}

	fmt.Println(string(file_data))
}