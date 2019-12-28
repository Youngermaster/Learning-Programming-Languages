#include <stdio.h>

int sumTwoIntegers(int a, int b);

int main(int argc, char const *argv[])
{
    int sum = sumTwoIntegers(10, 8);
    printf("The sum of 10 and 8 is: %d.\n", sum);
    return 0;
}

int sumTwoIntegers(int a, int b) {
    return a + b;
}