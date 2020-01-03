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
	file, err := os.Open("assets/file.txt")

	defer func() {
		file.Close()
		fmt.Println("Defer")
	}()

	if err != nil {
		fmt.Println("There was an error")
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
