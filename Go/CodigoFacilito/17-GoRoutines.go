package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	myString := "Myrtle"
	go printStringSlowly(myString)
	fmt.Println("I'm waiting...")
	var wait string
	fmt.Scanln(&wait)
}

func printStringSlowly(s string)  {
	chain := strings.Split(s, "")
	for _, char := range chain {
		time.Sleep(1000 * time.Millisecond)
		fmt.Println(char)
	}
}
