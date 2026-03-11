#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int np2,np1,np50,np20,np10,np5,argent;
    printf("Veuillez entrer la somme à rendre (exprimée en cents)\n");fflush(stdout);
    scanf("%d", &argent);
    np2=argent/200;
    argent=argent%200;
    np1=argent/100;
    argent = argent%100;
    np50 = argent/50;
    argent = argent%50;
    np20 = argent/20;
    argent = argent%20;
    np10 = argent/10;
    argent=argent%10;
    np5=argent/5;
    if(np2>=1)
    {
    printf("Il faut %d piece 2 EUR\n", np2);
    }
    if(np1>=1)
    printf("Il faut %d pieces de 1 EUR\n", np1);
    if(np50>=1)
    printf("Il faut %d pieces de 50 cents\n", np50);
    if(np20>=1)
    printf("Il faut %d pieces de 20 cents\n", np20);
    if(np10>=1)
    printf("Il faut %d pieces de 10 cents\n", np10);
    if(np5>=1)
    printf("Il faut %d pieces de 5 cents\n", np5);
    printf("fin");
    return 0;
}