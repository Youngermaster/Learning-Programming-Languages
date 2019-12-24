#include <stdio.h>

int main(int argc, char const *argv[]) {
    int myIntegerArray [4] = {0, 1, 2, 3};
    char myCharArray [5] = "Juan";

    printf("-> The integer array values are: %d, %d, %d, %d.\n",
    myIntegerArray[0], myIntegerArray[1], myIntegerArray[2], myIntegerArray[3]);

    printf("-> The char arry values are: %s.\n", myCharArray);

    return 0;
}
