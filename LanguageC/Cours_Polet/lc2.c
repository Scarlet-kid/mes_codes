#include <stdio.h>
#include <stdlib.h>

typedef struct _maillon
{
    int valeur;
    struct _maillon * suivant;
} Maillon;

typedef struct _lc
{
    Maillon *tete;
    int nbElt;
} LCint;

LCint CreerLCint()
{
    LCint liste;
    liste.tete = NULL;
    liste.nbElt = 0;
    return liste;
}

Maillon* creerMaillon(int val)
{
    Maillon* adrMaillon;
    adrMaillon = (Maillon*) malloc(sizeof(Maillon));
    adrMaillon->valeur = val;
    adrMaillon->suivant = NULL;

    return adrMaillon;
}

_Bool estVide(LCint liste)
{
    return liste.tete == NULL;
}

LCint ajouterValeur(LCint liste, int val)
{
    if(estVide(liste))
    {
        liste.tete = creerMaillon(val);
    }
    else
    {
        Maillon* ptr=liste.tete;
        while (ptr->suivant!=NULL)
        {
            ptr = ptr->suivant;
        }
        ptr->suivant = creerMaillon(val);
    }
    liste.nbElt ++;
    return liste;
}

void afficher(LCint liste)
{
    printf("[");
    if(!estVide(liste))
    {
        Maillon* ptr = liste.tete;
        while (ptr!=NULL)
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

Maillon* rechercher(LCint liste, int val)
{
    _Bool trouve = 0;
    Maillon* ptr = liste.tete;
    _Bool fini = ptr == NULL;
    while (!trouve)
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
    Maillon* aDetruire;
    aDetruire = rechercher(liste,val);
    if(aDetruire != NULL)
    {
        Maillon* ptr = liste.tete;
        if(aDetruire == ptr)
        {
            liste.tete = liste.tete->suivant;
        }
        else
        {
            while (ptr->suivant!=aDetruire)
            {
                ptr = ptr->suivant;
            }
            ptr->suivant = ptr->suivant->suivant;
        }
        liste.nbElt --;
    }
    return liste;
}

