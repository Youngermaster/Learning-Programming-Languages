package main

import "fmt"

func main() {
	// ! To copy an array or a slice you need almost a minimum lenght.
	slice := []int{1, 2, 3, 4}
	sliceCopyEmpty := make([]int, 0, 4)
	sliceCopyCorret := make([]int, len(slice), cap(slice)*2)

	copy(sliceCopyCorret, slice)
	copy(sliceCopyEmpty, slice)
	fmt.Println("Slice:", slice)
	fmt.Println("Slice Copy Empty:", sliceCopyEmpty)
	fmt.Println("Slice copied correct:", sliceCopyCorret)
}
