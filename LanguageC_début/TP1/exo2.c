#include <stdio.h>

void remplire(int *tab, int t)
{
    for(int i = 0; i < t; i = i + 1)
    {
        printf("saisir une valeur entiere > ");
        
        scanf("%d", &tab[i]); /* correction : la fct scan attend a recevoir une adresse mémoire en second paramètre */
    }
}

void afficher(int *arr, int s)
{
    printf("[");
    for(int i = 0; i < ; i = i + 1)/* débordement du tableau, j'ai enlevé le signe de l'égalité*/
    {
        printf("%d", arr[i]);
        if(i < s - 1)
        {
            printf(", ");
        }
    }
    printf("]");
}

int main(int argc, char **argv, char **env)
{
    int liste[4];

    
    remplire(liste, 4); /*appele de la fonction sans [4] qui correspond a un int or qu' on attend une adresse mémore.*/
    
    printf("les valeurs de la liste sont : ");
    afficher(liste, 4);
    printf("\n");

    return 0;
}