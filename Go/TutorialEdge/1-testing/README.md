## How to execute it?

run

    go test tests/function_test.go -v

you will see something like this:

- If it works:

        === RUN   TestSumNumberByTwo
        --- PASS: TestSumNumberByTwo (0.00s)
        === RUN   TestTableSumNumberByTwo
        --- PASS: TestTableSumNumberByTwo (0.00s)
        PASS
        ok      command-line-arguments  0.003s

if it doesn't work:

        === RUN   TestSumNumberByTwo
        --- PASS: TestSumNumberByTwo (0.00s)
        === RUN   TestTableSumNumberByTwo
        --- FAIL: TestTableSumNumberByTwo (0.00s)
            function_test.go:29: [TEST FAILED]: { 4421 } inputed,{ 4422 } expected, { 4423 } received
            function_test.go:29: [TEST FAILED]: { 9999 } inputed,{ 10000 } expected, { 10001 } received
        FAIL
        FAIL    command-line-arguments  0.004s
        FAIL