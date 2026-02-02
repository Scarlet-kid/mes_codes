#include <stdio.h>
#include "chaine.h"

int main()
{
    char t1[256] = {};
    char t2[256] = {};
    printf("Saisir une chaine :");
    scanf("%s",&t1);
    printf("La longueur de la chaine saisie est %d\n",longueur(t1));
    copie(t2,t1);
    printf("Contenu de t2 est %s\n",t2);

}