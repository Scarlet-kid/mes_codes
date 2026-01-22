#include <stdio.h>

float valeur_absolue(float val){
  if (val<0){
    return -val;
  }
  else{
      return val;
  }
}

int main(){
  float res;
  printf("Saisir une valeur :");
  scanf("%f",&res);
  printf("La valeur absolue de est %f\n",valeur_absolue(res));
}

