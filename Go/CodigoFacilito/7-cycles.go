package main

func main() {
	// * For cycle
	println("========= For Cycle =========")
	for index := 0; index < 5; index++ {
		println("Index: ", index)
	}

	// * Simulating the while cycle
	println("========= While Cycle =========")
	whileIndex := 0
	for whileIndex < 5 {
		println("Index: ", whileIndex)
		whileIndex++
	}
	// * Weird For cycle
	println("========= Weird For cycle =========")
	weirdForIndex := 0
	for {
		if weirdForIndex == 2 {
			weirdForIndex++
			continue
		}

		println("Index: ", weirdForIndex)
		weirdForIndex++

		if weirdForIndex > 5 {
			break
		}
	}
}
