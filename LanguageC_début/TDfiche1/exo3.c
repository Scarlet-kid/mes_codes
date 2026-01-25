#include <stdio.h>

int verifie_iterative(int val1,int val2)
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

int verifie_recurssive(int val1,int val2)
{
  int res;
  printf("Saisir une valeur entre %d et %d :",val1,val2);
  scanf("%d",&res);
  if(res<val1 || res>val2)
  {
    printf("Saisie incorrecte\n");
    return verifie_recurssive(val1, val2);
  }

  else
  {
      return res;
  }
}


int main(){
  int choix;
  printf("Quelle version voulez-vous tester ?(1 -> itérative et 2 -> recurssive):");
  scanf("%d",&choix);
  if (choix == 1)
  {
    printf("%d\n",verifie_iterative(1,10));
  }
  else
  {
    printf("%d\n",verifie_recurssive(1,10));
  }
  return 0;
}
