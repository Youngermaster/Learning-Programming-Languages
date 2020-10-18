#include <stdio.h>

struct Person
{
    int gpa;
    int age;
} juan, elYounger;

int main(int argc, char const *argv[])
{
    juan.age = 18;
    juan.gpa = 4;

    elYounger.age = 19;
    elYounger.gpa = 5;

    printf("Juan: Age = %d, gpa = %d.\n", juan.age, juan.gpa);
    printf("ElYounger: Age = %d, gpa = %d.\n", elYounger.age, elYounger.gpa);
    return 0;
}
