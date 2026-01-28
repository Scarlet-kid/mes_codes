#include <stdio.h>

void afficher2(float *tab, int taille){
    int i;
    printf("[");
    for ( i = 0; i < taille; i++)
    {
        printf("%f",tab[i]);
        if (i<taille-1)
        {
            printf(",");
        }
        
    }
    printf("]\n");
    
}

float somme2(float *tab, int taille){
    float somme = 0.0;
    int i;
    for ( i = 0; i < taille; i++)
    {
        somme = somme + tab[i];
    }
    return somme;
}

int main(){
    float myTab[10] =  {1,2,3,5,4,6,7,8,9,0};
    printf("myTab = ");
    afficher2(myTab,5);
    printf("La somme des valeurs vaut : %f\n",somme2(myTab,5));
    return 0;
}