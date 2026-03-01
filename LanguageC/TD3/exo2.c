#include <stdio.h>
#include <stdlib.h>

int concatene(int tab1[],int size1,int tab2[],int size2)
{
  int *tab3;
  tab3 = malloc((size1+size2)*sizeof(int));
  int i = 0;
  for(int j=0;j<size1;j++,i++)
  {
    tab3[i] = tab2[j];
  }

  for (int j = 0; j < size2; j++, i++)
  {
    tab3[i] = tab2[j];
  }
  
  return tab3;
}

int main()
{
  int tab1[3] = {1,2,3};
  int tab2[4] = {4,5,6,5};
  // je ne passe jamais un tableau en param mais l'addresse de son premier element
  concatene(tab1,3,tab2,4);
  return 0;
}
