#include <stdio.h>

int main(){
    int nais,age;
    printf("Tu es née dans quelle année : ");
    scanf("%d",&nais);
    nais = 2026-nais;
    printf("Cette année tu auras ou tu as déja %d ans\n",nais);
    return 0;
}