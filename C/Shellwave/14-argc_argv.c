#include <stdio.h>

int main(int argc, char const *argv[])
{
    int counter;
    printf("-> Argument counter = %d.\n", argc);

    printf("-> Argument values:\n");

    for (counter = 0; counter < argc; counter++)
        printf("argv[%d] = %s\n", counter, argv[counter]);

    return 0;
}
