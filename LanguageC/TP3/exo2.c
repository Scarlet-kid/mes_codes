#include <stdio.h>

typedef struct
{
    int jour;
    int mois;
    int annee;
}Date;

Date CreerDate(int monJours, int MonMois, int MonAnnee)
{
    Date maDate;
    maDate.jour = monJours;
    maDate.mois = MonMois;
    maDate.annee = MonAnnee;
    return maDate;
}

void afficher_date(Date d)
{
    printf("%d-%d-%d\n",d.jour,d.mois,d.annee);
}

typedef struct 
{
    char* nom;
    char* prenom;
    Date naissance;
}Personne;

Personne CreerPersonne(char*Monnom, char*Monprenom, Date Manaissance)
{
    Personne maPersonne;
    maPersonne.nom = Monnom;
    maPersonne.prenom = Monprenom;
    maPersonne.naissance = Manaissance;
}

void afficher_Personne(Personne p)
{
    printf("%s-%s-%s\n",p.nom,p.prenom,p.naissance);
}


