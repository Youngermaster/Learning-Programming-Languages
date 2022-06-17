package main

import (
	"bufio"
	"fmt"
	"net/http"
	"strconv"
	"time"
)

func hi(num int) {
	fmt.Println("Hi", num)
	time.Sleep(1000 * time.Millisecond)
}

func simulation_one() {
	for i := 0; i < 10; i++ {
		go hi(i)
	}
	
	var s string
	fmt.Scan(&s)
}

func get(num int) {
	resp, err := http.Get("https://jsonplaceholder.typicode.com/todos/" + strconv.Itoa(num))

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()
	fmt.Println("Status:", resp.Status)

	scanner := bufio.NewScanner(resp.Body)

	for i := 0; scanner.Scan(); i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}

func simulation_two() {
	for i := 0; i < 100; i++ {
		go get(i)
	}
	
	var s string
	fmt.Scan(&s)
}

func main() {
	// simulation_one()
	simulation_two()
}