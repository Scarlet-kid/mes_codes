#include <stdio.h>

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

void remplirFibo(int t[],int n)
{
  if(n>1)
  {
    t[0] = 0;
    t[1] = 1;
    for(int i = 2; i <= n-1; i++)
    {
      t[i] = fiboR(i);
    }
  }
}

int main(void)
{
  int myTab[7];
  remplirFibo(&myTab[0],7);
  for(int i=0;i<7;i++)
  {
    printf("myTab[%d] = %d\n",i,myTab[i]);
  }
  return 0;
}
