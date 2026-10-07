#include <stdio.h>
#include <stdlib.h>

typedef struct
{
  int * data;
  int taille ;
  int pos;
} TabListInt;

TabListInt creerTabListInt()
{
  TabListInt tli;
  tli.taille = 10;
  tli.pos = -1; //ya rien dedans
  tli.data = (int *) malloc(10*sizeof(int));
  return tli;
}

TabListInt append(TabListInt tli, int val)
{
  if(tli.pos == tli.taille-1)
  {
   int * noucTab = (int*) malloc(2*tli.taille*sizeof(int));
   for (int i=0; i<tli.taille;i++)
   {
      int nouvTab[100];
      nouvTab[i] = tli.data[i];
   }
   free(tli.data);
   tli.data = nouvTab;
   tli.taille = tli.taille*2;
  }
  tli.pos = tli.pos+1;
  tli.data[tli.pos+1] = val;
  return tli;
}

void printTabListInt(TablistInt tli)
{
  printf("[");
  for int i = 0;i<=tli.pos;i++)
  {
    printf("%d",tli.data[i])
    if (i <t li.pos)
    {
      print(", ");
    }
  }
  printf("]");
}

int int main()
{
  TabListInt maListe;
  maListe = creerTabListInt();
  maListe = append(maListe,5);
  maListe = append(maListe,10);
  maListe = append(maListe,15);
  printTabListInt(maListe);
  printf("\n");
  return 0;
}
