package tests

import (
	"testing"

	"../functions"
)

func TestSumNumberByTwo(t *testing.T) {
	if functions.SumNumberByTwo(4) != 6 {
		t.Error("[TEST FAILED] Expected 4 + 2 equals to 6")
	}
}

func TestTableSumNumberByTwo(t *testing.T) {
	var tests = []struct {
		input    int
		expected int
	}{
		{2, 4},
		{-1, 1},
		{4421, 4423},
		{9999, 10001},
	}

	for _, test := range tests {
		output := functions.SumNumberByTwo(test.input)
		if output != test.expected {
			t.Error("[TEST FAILED]: {", test.input, "} inputed,{",
				test.expected, "} expected, {", output, "} received")
		}
	}
}

func TestSumTwoNumbers(t *testing.T) {
	if functions.SumTwoNumbers(2, 6) != 8 {
		t.Error("[TEST FAILED] Expected 2 + 6 equals to 8")
	}
}
