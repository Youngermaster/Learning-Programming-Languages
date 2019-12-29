package main

import "fmt"

func main() {
	var x, y *int
	integer := 5

	x = &integer
	y = &integer

	*x = 8
	fmt.Println("X address:", x)
	fmt.Println("Y address:", y)

	fmt.Println("X value:", *x)
	fmt.Println("Y value:", *y)
}