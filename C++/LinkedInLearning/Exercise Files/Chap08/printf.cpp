// printf.cpp by Bill Weinman <http://bw.org/>
// updated 2002-06-24
#include <cstdio>

int main()
{
    int i = 5;
    long int li = 1234567890L;
    const char * s = "This is a string.";
    printf("i is %d, li is %ld, s is %s\n", i, li, s);
    return 0;
}
