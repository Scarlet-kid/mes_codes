#include <stdio.h>

int main()
{
  int i, j;
  printf("X\t");
  for (j=0; j<=10; j++)
  {
    printf("%d\t",j);
  }
  printf("\n");
  for(i=0; i<=10; i++)
  {
    printf("%d\t",i);
    for ( j = 0; j <= 10; j++)
    {
      printf("%d\t", i*j);
    }
    printf("\n");
  }
  return 0;
}
