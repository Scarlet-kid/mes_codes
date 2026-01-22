#include <stdio.h>

void saisieBorneeIter(int mini, int maxi, int *value)
{
  fini = 0
  int res;
  while(!fini)
  {
    printf("Saisir une valeur entre %d et %d:",mini,maxi);
    scanf("%d",res);
    if (res<mini || res>maxi)
    {
      printf("Saisie incorrect");
    }
    else
    {
      *value = res;
    }
  }
}
