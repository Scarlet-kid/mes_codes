#include <stdio.h>

void accumuler(int *variable, int valeur){
    *variable = valeur + *variable;
}

int main(){
    int a;
    int i;
    a = 5;
    for ( i = 1; i <= 3; i++)
    {
        accumuler(&a,i);
        printf("a = %i\n",a);
    }

    return 0;
}