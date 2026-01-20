#include <stdio.h>

int main(void){
    float a = 6.25;
    float b;
    float *c; // Il y aura un adresse dans cette variable.
    c = &a;
    b = *c + 4;
    printf("b = %f\n",b);
    return 0;
}