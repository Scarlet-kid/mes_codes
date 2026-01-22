#include <stdio.h>

int main(void){
  float val;
  printf("Saisir une valeur réelle:");
  scanf("%f",&val);
  if (val<0){
    printf("%f\n",-val);
  }
  else{
      printf("%f\n",val);
  }
  return 0;
}

