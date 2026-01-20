#include <stdio.h>

int minimum(int,int);

int main(void){
    int val1,val2 ;
    printf("Saisir une valeur entière :");
    scanf("%d",&val1);
    printf("Saisir une valeur entière :");
    scanf("%d",&val2);
    printf("La plus petite des deux valeurs est %i\n",minimum(val1,val2));
    return 0;
}

int minimum(int x, int y){
    if (x<y){
        return x;
    }
    else{
        return y;
    }
}