#include <stdio.h>
#include <string.h>

void myGets(char *s,int tmax)
{
    int i;
    fgets(s, tmax, stdin);
    if(s[strlen(s)-1] == '\n')
    {
        s[strlen(s)-1] = '\0'; // Quand on trouve un saut de ligne fin.
    }
}

int main()
{
    char chaine[80];
    printf("Saisir une chaine de caractère > ");
    myGets(chaine, 79);
    printf("La chaine = %s",chaine);
    printf("<fin de la chaine saisie\n");
    return 0;
}