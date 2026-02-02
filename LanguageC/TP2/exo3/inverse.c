#include <stdio.h>
#include <stdlib.h>

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

int main() {
    char saisie[100];
    
    printf("Entrez une chaine : ");
    if (fgets(saisie, sizeof(saisie), stdin)) {
        
        
        int l = longueur(saisie);
        if (l > 0 && saisie[l-1] == '\n')
        {
            saisie[l-1] = '\0';
        }

        char* resultat = inverser(saisie);

        if (resultat != NULL) {
            printf("Chaine inversee : %s\n", resultat);
            free(resultat);
        }
    }
    return 0;
}