#include <stdio.h>
#include <math.h>
#define NFOIS 5

int main() {
    int i;
    float x;
    float racx;
    printf("Bonjour\n");
    printf("Je vais vous calculer %d racine carrée\n",NFOIS);
    for (i=0; i<NFOIS; i++) {
        printf("Donnez un nombre :");
        scanf("%f",&x);
        if (x<0.0)
            printf("Le nombre %f ne possède pas de racine carrée\n",x);
        else {
            racx = sqrt(x);
            printf("Le nombre %f a pour racine carrée %f",x,racx);
        }
    }
    printf("Travail terminé - Au revoir");
}
