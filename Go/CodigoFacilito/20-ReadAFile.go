package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("assets/file.txt")

	if err != nil {
		fmt.Println("There was an error")
	}

	scanner := bufio.NewScanner(file)

	lineIndex := 0
	for scanner.Scan() {
		fmt.Println("Line", lineIndex, ":", scanner.Text())
		lineIndex++
	}

	file.Close()
}
