#include <stdio.h>

int verifie(int val1,int val2)
{
  _Bool fini = 0;
  int val;
  while(!fini)
  {
    printf("Saisir une valeur entre %d et %d:",val1,val2);
    scanf("%d",&val);
    if(val<val1 || val>val2)
    {
      printf("Saisie incorrecte\n");
    }
    else
    {
      fini = 1;
    }
  }
  return val;
}

int main(){
  printf("%d\n",verifie(1,10));
  return 0;
}
