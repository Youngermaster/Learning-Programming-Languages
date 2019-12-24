#include <stdio.h>

int main(int argc, char const *argv[]) {
    char message[12] = "Hello world";

    printf("The message is: %s\n", message);
    printf("The position 2 of the array is: %c\n", message[1]);
    printf("The ASCII value of the position 2 of the array is: %d\n", message[1]);
    return 0;
}