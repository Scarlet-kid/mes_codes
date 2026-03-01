#include <stdio.h>
#include <stdlib.h>

typedef struct _maillon
{
    int valeur;
    struct _maillon * suivant;
} Maillon;

typedef struct _lc
{
    Maillon* tete;
    int nbElt;
} LCint;

LCint creerLCint()
{
    LCint liste;
    liste.tete = NULL;
    liste.nbElt = 0;
    return liste;
}

Maillon *creerMaillon(int val)
{
    Maillon* adrMailllon;
    adrMailllon = (Maillon*)malloc(sizeof(Maillon));
    adrMailllon->valeur = val;
    adrMailllon->suivant = NULL;
    return adrMailllon;
}

_Bool estVide(LCint liste)
{
    return liste.tete == NULL;
}

void afficher(LCint liste)
{
    printf("[");
    if(!estVide(liste))
    {
        Maillon * ptr = liste.tete;
        while(ptr!=NULL)
        {
            printf("%d",ptr->valeur);
            if(ptr->suivant!=NULL)
            {
                printf(", ");
            }
            ptr = ptr->suivant;
        }
    }
    printf("]");
}

LCint ajouterVal(LCint liste, int val)
{
    if(estVide(liste))
    {
        liste.tete = creerMaillon(val);
    }
    else
    {
        Maillon * ptr = liste.tete;
        while (ptr->suivant!=NULL)
        {
            ptr = ptr->suivant;
        }
        ptr->suivant = creerMaillon(val);
    }
    liste.nbElt ++;
    return liste;
}

Maillon * rechercher(LCint liste, int val)
{
    _Bool trouve = 0;
    Maillon * ptr = liste.tete;
    _Bool fini = ptr == NULL;
    while (!fini)
    {
        if(ptr->valeur == val)
        {
            trouve = 1;
            fini = 1;
        }
        else
        {
            ptr = ptr->suivant;
            fini = ptr == NULL;
        }
    }
    if(trouve)
    {
        return ptr;
    }
    else
    {
        return NULL;
    }
}

LCint supprimer(LCint liste, int val)
{
    Maillon * aDetruire;
    aDetruire = rechercher(liste, val);
    if(aDetruire != NULL)
    {
        Maillon * ptr = liste.tete;
        if(aDetruire == ptr)
        {
            liste.tete = liste.tete->suivant;
        }
        else
        {
            while (ptr->suivant != NULL)
            {
                ptr = ptr->suivant;
            }
            ptr->suivant = ptr->suivant->suivant;
        }
        liste.nbElt --;
    }
    return liste;
}

int main()
{
    LCint maListe;
    maListe = creerLCint();
    maListe = ajouterVal(maListe,5);
    maListe = ajouterVal(maListe,15);
    maListe = ajouterVal(maListe,10);
    afficher(maListe);
    printf("\n");
    return 0;
}