package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	execution := readFile()
	fmt.Println(execution)
}

func readFile() bool {
	file, err := os.Open("assets/fisle.txt")

	defer func() {
		file.Close()
		fmt.Println("Defer")
		fmt.Println("[Error Here!]:", recover())
	}()

	if err != nil {
		fmt.Println("There was an error")
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	lineIndex := 0
	for scanner.Scan() {
		fmt.Println("Line", lineIndex, ":", scanner.Text())
		lineIndex++
	}

	if true {
		return true
	}
	
	fmt.Println("I never execute")
	return true
}
