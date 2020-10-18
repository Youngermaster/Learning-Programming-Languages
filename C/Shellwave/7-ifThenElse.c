#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n = 10;

    if (n >= 5)
    {
        printf("-> n is greater than or equal to 5.\n");
    }
    else
    {
        printf("-> Conditional statement 1 failed.\n");
    }

    if (n <= 5)
    {
        printf("-> n is less than or equal to 5.\n");
    }
    else
    {
        printf("-> Conditional statement 2 failed.\n");
    }

    return 0;
}
