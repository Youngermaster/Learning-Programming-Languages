package main

import "fmt"

func main() {
	x := 10
	y := 10
	if x > y {
		fmt.Printf("%d is bigger than %d.\n", x, y)
	} else if x < y {
		fmt.Printf("%d is less than %d.\n", x, y)
	} else {
		fmt.Printf("%d is equal to %d.\n", x, y)
	}
}