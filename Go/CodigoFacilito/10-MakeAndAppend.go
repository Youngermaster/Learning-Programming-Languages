package main

import "fmt"

func main() {
	slice := make([]int, 2, 4)

	fmt.Println("Slice 1:", slice)

	slice = append(slice, 2)
	fmt.Println("Slice 1 + append:", slice)

	fmt.Println("Slice 1 length:", len(slice))
	fmt.Println("Slice 1 capacity: ", cap(slice))
}