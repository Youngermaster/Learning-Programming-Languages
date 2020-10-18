#include <stdio.h>

int main(int argc, char *argv[])
{
    char y = 'y';
    int k = 24;
    float myFloat;
    double myDouble;
    long int myLongInt;

    printf(">\t\tSize of each data type\t\t <\n");
    printf("Size of char: %lo\n", sizeof(y));
    printf("Size of int: %lo\n", sizeof(k));
    printf("Size of float: %lo\n", sizeof(myFloat));
    printf("Size of double: %lo\n", sizeof(myDouble));
    printf("Size of long int: %lo\n", sizeof(myLongInt));

    return 0;
}