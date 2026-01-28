#include <stdio.h>
int fiboI(int n)
{
  if(n<2)
  {
    return n;
  }
  else
  {
    int f;
    int f1 = 1;
    int f2 = 0;
    int i;
  for (i=1;i<n;i++)
  {
    f = f1+f2;
    f2 = f1;
    f1 = f;
  }
  return f1;
  }
}


int fiboR(int n)
{
  if (n == 0 || n == 1)
  {
    return n;
  }
  else
  {
    return fiboR(n-1) + fiboR(n-2);
  }
}

int main(void)
{
  int choix;
  printf("Votre (choix 1->Itérative et 2->Récurssive):");
  scanf("%d",&choix);
  if (choix == 1)
  {
    int res;
    printf("Saisir une valeur :");
    scanf("%d",&res);
    printf("fibo de %d est %d\n",res,fiboI(res));
  }
  else
  {
    int res;
    printf("Saisir une valeur :");
    scanf("%d",&res);
    printf("fibo de %d est %d\n",res,fiboR(res));
  }
  return 0;
}

