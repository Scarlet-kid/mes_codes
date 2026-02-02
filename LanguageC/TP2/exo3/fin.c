#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int longueur(char *s)
{
    int i = 0;
    if(s==NULL) // on verifie si le pointeur est null.
    { 
        return 0;
    }
    else
    {
        while (s[i] != '\0')
        {
            i++;
        } 
        return i;
    } 
}



char* inverser(char* s) {
    if(s == NULL)
    {
        return NULL;
    } 

    int len = longueur(s);
    char* destination = malloc((len + 1) * sizeof(char));
    
    if(destination == NULL)
    {
        return NULL;
    } 

    for (int i = 0; i < len; i++)
    {

        destination[i] = s[len - 1 - i];
    }

    destination[len] = '\0';

    return destination;
}


void inverserCasse(char *s)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] >= 'A' && s[i] <= 'Z')
        {
            s[i] += 32;
        }
        else
        {
            if (s[i] >= 'a' && s[i] <= 'z')
            {
                s[i] -= 32;
            }
        }
    }
}


int main() {
    char saisie[100];
    
    printf("Entrez une chaine : ");
    if (fgets(saisie, sizeof(saisie), stdin)) {
        

        int l = longueur(saisie);
        if (l > 0 && saisie[l-1] == '\n')
        {
            saisie[l-1] = '\0';
        } 

        // 1. Affichage de l'inverse
        char* inv = inverser(saisie);
        if (inv)
        {
            printf("Ordre inverse : %s\n", inv);
            
            // 2. Vérification Palindrome
            if (strcmp(saisie, inv) == 0)
            {
                printf("C'est un palindrome !\n");
            } 
            else 
            {
                printf("Ce n'est pas un palindrome.\n");
            }
            free(inv);
        }
        inverserCasse(saisie);
        printf("Casse inversee : %s\n", saisie);
    }
    return 0;
}