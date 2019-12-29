package main

import "fmt"

func main() {
	var sliceNull []int
	if sliceNull == nil {
		fmt.Println("The Slice is null")
	} else {
		fmt.Println(sliceNull)
	}

	slice := []int{1, 2}
	if slice == nil {
		fmt.Println("The Slice is null")
	} else {
		fmt.Println(slice)
		fmt.Println("Slice len", len(slice))
	}

	array := [4]int{0, 1, 2, 3}
	sliceArry := array[0:3]
	fmt.Println(sliceArry)
}
