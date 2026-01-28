#include <stdio.h>

void afficher1(float tab[5]){
    int i;
    printf("[");
    for ( i = 0; i < 5; i++)
    {
        printf("%f",tab[i]);
        if (i<4)
        {
            printf(",");
        }
        
    }
    printf("]\n");
    
}

float somme1(float tab[5]){
    float somme = 0.0;
    int i;
    for ( i = 0; i < 5; i++)
    {
        somme = somme + tab[i];
    }
    return somme;
}

int main(){
    float myTab[5] = {1.0,3.9,4.0,6.5,5.6};
    printf("myTab = ");
    afficher1(myTab);
    printf("La somme des valeurs vaut : %f\n",somme1(myTab));
    return 0;
}