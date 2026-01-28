#include <stdio.h>
#include <stdlib.h>

typedef struct
{
  int * data; //Le tableau en soi.
  int taille ; // lla taille du tableau
  int pos; //La position du dernier élément ajouté.
} TabListInt; //On définit la structure de notre TabListInt.

TabListInt creerTabListInt() // On la crée vu que on l'a déja come objet notre fonction le renverra.
{
  TabListInt tli; //On renomme notre objet TabListInt en tli(souci de flexbiliser la manipulation)
  tli.taille = 10;

  tli.pos = -1; //ya rien dedans par défaut cest -1
  tli.data = (int *) malloc(tli.taille*sizeof(int)); //allouer de la mémoire pour un entier. 10 fois la taille d'un objet int 
  return tli;
}

TabListInt append(TabListInt tli, int val) // Pour ajouter.
{
  if(tli.pos == tli.taille-1) // En gros quand c'est plein.
  {
   int * nouvTab = (int*) malloc(2*tli.taille*sizeof(int));// On réalloue un nouveau espace mémouire. Doubler l'allouement de la mémoire si cest plein, pour eviter de remplir quand c'est plein.
   for (int i=0; i<tli.taille;i++)
   {
      nouvTab[i] = tli.data[i];
   }
   free(tli.data); //libérer l'espace mémoire non utilisé quand on aura fais .
   tli.data = nouvTab; // Donc je pense en gros on modifie une liste et on le plaque dans tli.data (pratique)
   tli.taille = tli.taille*2; //On double la taille.
  }
  // Quand ce n'est pas plein.
  tli.pos = tli.pos+1;
  tli.data[tli.pos] = val;
  return tli;
}

void printTabListInt(TabListInt tli)
{
  printf("[");
  for(int i = 0; i<=tli.pos; i++) //La position du dernier élément enregistrer.
  {
    printf("%d",tli.data[i]);
    if (i <tli.pos) //avant dernier élément.
    {
      printf(", ");
    }
  }
  printf("]");
}

int main()
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
// pratique les alloc dynamique !!!!