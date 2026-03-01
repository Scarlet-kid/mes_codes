#include <stdio.h>
#include <stdlib.h>

typedef struct
{
  int * data; //Le tableau en soi.
  int taille ; // la taille du tableau
  int pos; //La position du dernier élément ajouté.
} TabListInt; //On définit la structure de notre TabListInt.

TabListInt creerTabListInt() // On la crée vu que on l'a déja come objet notre fonction le renverra.
{
  TabListInt tli; //On cree un objet tab list int appelé tli.
  tli.taille = 10; // taille par défaut.

  tli.pos = -1; //ya rien dedans par défaut cest -1 .
  tli.data = (int*) malloc(tli.taille*sizeof(int)); //allouer de la mémoire pour un entier. 10 fois la taille d'un objet int 
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
   free(tli.data); //libérer l'espace mémoire de notre tablistint de base car on a doublé l'espace mémoire da,sune autre tablistint pour y stocker des donnée de celle ci ainsi que ceux qui sont supplémentaire.
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

TabListInt supprimer(TabListInt TLI, int val)
{
    int index = 0;
    int trouve = 0;
    while (trouve == 0 && index <= TLI.pos) //On a pas trouvé et on est pas arrivé a la fin de la liste,
    {
        if (TLI.data[index] == val) // SI on a trouvé a un index
        {
            trouve = 1; // on a trouvé on sort de la boucle.
        }
        else
        {
            index++; // on passe a l'indice suivant.
        }
    }

    if (trouve) // Si on a trouvé
    {
        int i = index; // On recupere la position de la valeur.
        while (i < TLI.pos)
        {
            TLI.data[i] = TLI.data[i + 1];
            i++;
        }
        TLI.pos--; // Polet il est trop fort .
    }

    return TLI;
}

void trier(TabListInt tli)
{
  int tmp;
  int i;
  int j;
  for(i=1;i<=tli.pos;i++)
  {
  tmp = tli.data[i];
  j=i;
  while(j>0 && tli.data[j-1]>tmp)
  {
    tli.data[j]=tli.data[j-1];
    j=j-1;
  }
  tli.data[j] = tmp;
  }
}

int main()
{
  TabListInt maListe;
  maListe = creerTabListInt();
  maListe = append(maListe,15);
  maListe = append(maListe,10);
  maListe = append(maListe,5);
  maListe = append(maListe,0);
  maListe = append(maListe,1);
  maListe = append(maListe,2);
  printTabListInt(maListe);
  trier(maListe);
  //maListe = supprimer(maListe,10);
  printTabListInt(maListe);
  printf("\n");
  //return 0;
}
// pratique les alloc dynamique !!!!
