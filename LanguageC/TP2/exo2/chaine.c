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

void copie(char *dest, char *source)
{
    int i = 0;
    if(dest==NULL || source==NULL) // on voit si un des pointeur est nul
    {
        return; //On quitte le prog
    }
    while (source[i] != '\0')
    {
        dest[i] = source[i];
        i = i + 1;
    }
    dest[i] = '\0';
}

char* reduire(char* s) 
{
    if(s==NULL)
    {
        return NULL;
    }
    int Slongueur = longueur(s);
    char *Macopie = malloc(sizeof(char)*Slongueur);
    if (Macopie==NULL)
    {
        return NULL;
    }
    copie(Macopie, s);
}

int main()
{
    
    char maChaine[] = "lolo";
    int resultat = reduire(maChaine);
    
    printf("La reduction de %s' est : %d\n", maChaine, resultat);
    
    return 0;
}

