#include <stdio.h>
#include <stdlib.h>

float moyenne(float tab[], int n)
{
    float somme = 0.0;
    int i;
    for(i=0; i<n; i++)
    {
        somme = somme + tab[i];
    }
    return somme/n;
}

float * saisirNotes(int n)
{
    float * t = (float *) malloc(n*sizeof(float));
    int i;
    for(i=0; i<n; i++)
    {
        printf("Saisir la note [%d]>",i);
        scanf("%f",&t[i]);
    }
    return t;
}

int main()
{
    int nb;
    float * notes;
    float moy;

    printf("Combien de notes ? :");
    scanf("%d",&nb);
    notes = saisirNotes(nb);
    moy = moyenne(notes, nb);

    printf("la moyenne des notes = %f\n",moy);
    return 0;
}

