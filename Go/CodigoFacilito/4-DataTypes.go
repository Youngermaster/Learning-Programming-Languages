package main

import("strconv");

func main() {
	age := 18;
	println("Int to String.");
	println("My ages is: " + strconv.Itoa(age));

	numberInString := "12";
	number, _ := strconv.Atoi(numberInString);
	println("String to Int.");
	print("12 + 2 = ");
	println(number + 2);
}