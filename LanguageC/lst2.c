#include <stdio.h>

void f(float tab[5]){
    printf("&tab[0] = %x, tab = %x\n",&tab[0],tab);
}

int main(){
    float myTab[10] = {1,2,3,5,4,6,7,8,9,0};
    f(myTab);
    printf("&myTab[0] = %x, myTab = %x\n",&myTab[0],myTab);
    return 0;
}