#include <stdio.h>

float moyenne(float* tab, int n)
{
    float somme = 0.0;
    for(int i = 0; i<n; i++)
    {
        somme = somme + tab[i];
    }
    return somme/n;
}

