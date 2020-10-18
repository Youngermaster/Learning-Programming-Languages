#include <stdio.h>

int sumTwoIntegers(int a, int b);

int main(int argc, char const *argv[])
{
    int (*myFunctionPointer)(int, int);
    myFunctionPointer = sumTwoIntegers;
    int sum = myFunctionPointer(9, 9);
    printf("9 + 9 = %d.\n", sum);
    return 0;
}

int sumTwoIntegers(int a, int b)
{
    return a + b;
}