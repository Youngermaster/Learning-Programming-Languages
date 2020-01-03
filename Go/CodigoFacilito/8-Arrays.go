package main

import "fmt"

func main() {
	array := [3]int{1, 2}
	array[2] = 20
	for index := 0; index < len(array); index++ {
		println("array[", index, "]", " = ", array[index])
	}

	matrix := [3][2]int{}
	println(matrix[0][0])
	fmt.Println(matrix)
}
