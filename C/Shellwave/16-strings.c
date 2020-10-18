#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char stringOne[24], stringTwo[24];
    int iterator, length;

    // Example 1
    sprintf(stringOne, "Hello world.");
    printf("-> Example 1\n%s\n", stringOne);

    // Example 2
    iterator = 4;
    sprintf(stringOne, "Value of iterator = %d.", iterator);
    printf("-> Example 2\n%s\n", stringOne);

    // Example 3
    length = strlen(stringOne);
    printf("-> Example 3\nLenght of String one: %d.\n", length);

    // Example 4
    strcpy(stringTwo, stringOne);
    printf("-> Example 4\nString Two: %s.\n", stringTwo);

    // Example 5
    memset(stringOne, 0, 24);
    memset(stringOne, 'a', 10);
    printf("-> Example 5\n>%s<\n", stringOne);

    return 0;
}