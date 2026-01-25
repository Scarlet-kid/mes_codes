#include <stdio.h>

float main(void)
{
    float res;
    printf("Saisir une valeur réelle :");
    scanf("%f",&res);
    if (res<0)
    {
        printf("La valeur absolue du nombre est %f\n",-res);
    }
    else
    {
        printf("La valeur absolue du nombre est %f\n",res);
    }
}