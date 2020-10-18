#include <stdio.h>

typedef int INT32;
typedef char MYCHAR;

typedef struct Element
{
    char id;
    float weight;
} ELEMENT;

int main(int argc, char const *argv[])
{
    INT32 i;
    MYCHAR fullName[25] = "Juan Manuel Young Hoyos";

    printf("-> INT32: %d.\n", i);
    printf("-> MYCHAR: %s.\n\n", fullName);

    ELEMENT gold, silver;

    gold.id = 1;
    gold.weight = 0.97;

    silver.id = 2;
    silver.weight = 0.81;

    printf("-> Gold: ID = %d, Weight = %f.\n", gold.id, gold.weight);
    printf("-> Silver: ID = %d, Weight = %f.\n", silver.id, silver.weight);
    return 0;
}
