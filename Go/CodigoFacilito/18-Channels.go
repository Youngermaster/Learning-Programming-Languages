package main

import "fmt"

func main() {
	myChannel := make(chan string)
	go func(channel chan string) {
		for {
			var name string
			fmt.Scanln(&name)
			channel <- name
		}
	}(myChannel)

	msg := <-myChannel
	fmt.Println("Channel message:", msg)
	msg2 := <-myChannel
	fmt.Println("Channel message:", msg2)
}
