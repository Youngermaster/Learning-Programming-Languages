#include <stdio.h>

int main(int argc, char const *argv[])
{
    int i = 0;

    printf("======= While =======\n");
    while (i < 10)
    {
        printf("-> i = %d.\n", i);
        i++;
    }

    i = 0;
    printf("======= Do While =======\n");
    do
    {
        printf("-> i = %d.\n", i);
        i++;
    } while (i < 10);

    return 0;
}