#include <stdio.h>
void trier( int t[], int n)
{
  int tmp;
  int i;
  int j;
  for(i=1;i<=n;i++)
  {
  tmp = t[i];
  j=i;
  while(j>0 && t[j-1]>tmp)
  {
    t[j]=t[j-1];
    j=j-1;
  }
  t[j] = tmp;
  }
}

void afficher(int t[], int n)
{
  printf("[");
  for(int i=0;i<n;i++)
  {
    printf("%d",t[i]);
    if(i < n-1)
    {
      printf(", ");
    }
  }

  printf("]");
}

int main()
{
  int myTab[6] = {6,5,4,3,2,1};
  afficher(myTab, 6);
  printf("\n");
  trier(myTab, 6);
  afficher(myTab, 6);
  printf("\n");
  return 0;
}