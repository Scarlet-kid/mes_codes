#include <stdio.h>
#include <stdlib.h>

typedef struct _maillon
{
    int valeur; // ici la valeur car un maillon cest une valeur et un suivant qui pointe vers le maillon suivant.
    struct _maillon *suivant; // Pointeur vers l'élément suivant, en gros le suivant est un pointeur vers un maillon(maillon suivant).
} Maillon;

typedef struct _lc
{
    Maillon *tete; //la tete meme est un pointeur vers un maillon car la tete est en soit un maillon dand lequel on a un maillon et le suivant.
    int nbElt; // le nombre d'élément de la lst chainée.
} LCint;

Maillon* creerMaillon(int v)
{
    Maillon* adrMaillon; //un pointeur de maillon.
    adrMaillon  = (Maillon*)malloc(sizeof(Maillon)); // on alloue la place pour un maillon.
    (*adrMaillon).valeur = v; // en gros la valeur du truc
    adrMaillon->suivant = NULL; // En gros rien dans le suivant pour le moment.

    return adrMaillon; // on retourne le truc.
} // ca ca va !

LCint creerLCint()
{
    LCint liste; 
    liste.tete = NULL;
    liste.nbElt = 0;
    return liste;
}

_Bool estVide(LCint liste)
{
    return liste.tete == NULL; //Pourquoi null ? je pense un mbelt == 0 fera aussi bien l'affaire.
}

LCint ajouterVal(LCint liste, int val)
{
    if(estVide(liste)) 
    {
        liste.tete = creerMaillon(val); // Si cest vide alors notre premier maillon est la tete.
    }
    else
    {
        Maillon * ptr = liste.tete;
        while (ptr->suivant != NULL)
        {
            ptr = ptr->suivant; //Pour que ca continue jusqu'a trouver un suivant qui est null.
        }
        ptr->suivant = creerMaillon(val); // on cree un maillon a ce suivant et le suivant de ce maillon est null.
    }
    liste.nbElt ++; // on increment le nb d'elément de la liste de 1.
    return liste;
}

void afficherListe(LCint liste)
{
    printf("["); //On ouvre les crochets
    if (! estVide(liste))  //Tant que la liste est pas vide.
    {
        Maillon* ptr = liste.tete; // Un pointeur de maillon meme champ qu'un maillon ordinaire.
        while (ptr!=NULL) // tant qu'il ya un maillon.
        {
            printf("%d",ptr->valeur); //On l'affiche.
            if(ptr->suivant!=NULL) // Tant qu'il ya un suivant 
            {
                printf(", "); //On met le point virgule
            }
            ptr = ptr->suivant; // Pour que ca continue sinon pas de condition d'arret et boucle infinie.
        }
    }
    printf("] "); // On ferme les crochets.
}

Maillon* rechercher(LCint liste, int val) // ca nous renvoie un maillon.
{
    _Bool trouve = 0; // Au debut, on na pas trouvé.
    Maillon *ptr = liste.tete; // un pointeur de maillon qui est par défaut la tete de notre liste chainéé
    _Bool fini = ptr == NULL; // En tout cas je comprend pas trop mais.....
    while (!fini) //tant qu'on a pas fini:
    {
        if (ptr->valeur == val) // si on trouve la valeur cherchée
        {
            trouve = 1; // on a trouvé
            fini = 1; // On a fini.
        }
        else
        {
            ptr = ptr->suivant; // On va vers le maillon suivant , la boucle doit continuer.
            fini = ptr == NULL; // En tout cas je comprend pas trop mais.....
        }
    }
    if(trouve)
    {
        return ptr; // On retourne l'adresse ou le maillon se trouve.
    }
    else
    {
        return NULL; // Il ya pas d'adresse pour ce maillon donc pointeur null.
    }
}

LCint supprimer(LCint liste, int val)
{
    
    Maillon * aDetruire; // un maillon a detruire l'element et son suivant .

    aDetruire = rechercher(liste,val); //On voit que la valeur du maillon a detruire est dans la liste. 
    if(aDetruire != NULL) // Si il y est,
    {
        Maillon* ptr = liste.tete; //un pointeur de maillon 
        if (aDetruire == ptr) // EN gros si ce qu'on veut detruire est la tete de la liste.
        {
            liste.tete = liste.tete->suivant; // la tete devient le suivant, sa valeur est detruite.
            //ptr = ptr.suivant;
        }
        else // si cest pas la tete,
        {
            while(ptr->suivant!=aDetruire) // On verifie le suivant
            {
                ptr = ptr->suivant; // pour que ca continue.
            }
            ptr->suivant = ptr->suivant->suivant; // Pour que ca continue le suivant de la tete devient le suivant du suivant de la tete ainsi de suite , je comprend.
        }
        liste.nbElt --; //Si on trouve le truc et on le detruit et on désincrement le nb d'elt de 1.
    }
    return liste;
}

int main()
{
    LCint maListe;
    maListe = creerLCint();
    maListe = ajouterVal(maListe,5);
    maListe = ajouterVal(maListe,10);
    maListe = ajouterVal(maListe,15);

    afficherListe(maListe);
    printf("\n");

    maListe = supprimer(maListe,10);
    maListe = supprimer(maListe,17);

    afficherListe(maListe);
    printf("\n");

    maListe = supprimer(maListe,15);

    afficherListe(maListe);
    printf("\n");

    maListe = supprimer(maListe,5);
    afficherListe(maListe);
    printf("\n");

    maListe = supprimer(maListe,5);
    afficherListe(maListe);
    printf("\n");

    return 0;
}
