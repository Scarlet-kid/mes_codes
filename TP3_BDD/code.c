#include <stdio.h>
void f(int*a,int b)
{
    *a=*a+1;
    b=b+1;
}

int main()
{
    int a=5;
    int b=6;
    printf("a=%d,b=%d",a,b);
    f(&a,b);
    printf("\n");
    printf("a=%d,b=%d",a,b);
    printf("\n");
}