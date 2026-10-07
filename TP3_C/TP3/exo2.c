#include <stdio.h>
#include <stdlib.h>


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

Personne CreerPersonne(char* Monnom, char *Monprenom, Date Manaissance)
{
    Personne maPersonne;
    maPersonne.nom = Monnom;
    maPersonne.prenom = Monprenom;
    maPersonne.naissance = Manaissance;
    return maPersonne;
}

void afficher_Personne(Personne p)
{
    printf("%s-%s ",p.nom,p.prenom);
    afficher_date(p.naissance);
}

void ajouterPfile1(Personne p)
{
    FILE* pf;
    pf  = fopen("exemple1.txt","w");
    fprintf(pf,"Nom: %s, prénom : %s naissance %d-%d-%d",p.nom,p.prenom,p.naissance.jour,p.naissance.mois,p.naissance.annee);
    fclose(pf);
}

void ajouterPfile2(Personne p)
{
    FILE* pf;
    pf  = fopen("exemple1.dat","ab");
    fwrite(&p,sizeof(Personne),1,pf);
    fclose(pf);
}




void demanderUtl1()
{
    Personne per;
    FILE* pf;
    pf  = fopen("exemple2.txt","w");
    int nb;
    printf("Combien de personnes voulez-voud ajouter?:");
    scanf("%d",&nb);
    for(int i=0;i<nb;i++)
    {
        char name[50];
        char surname[50];
        int j;
        int m;
        int a;
        printf("nom:");
        scanf("%s",name);
        printf("prenom:");
        scanf("%s",surname);
        printf("jour de naissance:");
        scanf("%d",&j);
        printf("mois de naissance:");
        scanf("%d",&m);
        printf("année de naissance:");
        scanf("%d",&a);
        fprintf(pf,"Nom: %s, prénom : %s naissance %d-%d-%d\n",per.nom=name,per.prenom=surname,per.naissance.jour=j,per.naissance.mois=m,per.naissance.annee=a);
    }
    fclose(pf);
}

void demanderUtl2()
{
    Personne per;
    FILE* pf;
    pf  = fopen("exemple2.dat","w");
    int nb;
    printf("Combien de personnes voulez-voud ajouter?:");
    scanf("%d",&nb);
    for(int i=0;i<nb;i++)
    {
        char name[50];
        char surname[50];
        int j;
        int m;
        int a;
        printf("nom:");
        scanf("%s",name);
        printf("prenom:");
        scanf("%s",surname);
        printf("jour de naissance:");
        scanf("%d",&j);
        printf("mois de naissance:");
        scanf("%d",&m);
        printf("année de naissance:");
        scanf("%d",&a);
        fwrite(&per,sizeof(Personne),nb,pf);
    }
    fclose(pf);
}

void recupererEtAfficher10() {
    FILE* pf = fopen("exemple2.txt", "r");
    if (pf == NULL) {
        printf("Erreur : Impossible d'ouvrir le fichier.\n");
        return;
    }

    char nom[50], prenom[50];
    int j, m, a;
    int compteur = 0;

    printf("\n--- Lecture du fichier (Format spécifique) ---\n");

    while (compteur < 10 && fscanf(pf, "Nom: %[^,], prénom : %s naissance %d-%d-%d\n", 
                                   nom, prenom, &j, &m, &a) == 5) {
        
        printf("Personne %d : %s %s né le %d/%d/%d\n", 
               compteur + 1, nom, prenom, j, m, a);
        compteur++;
    }

    if (compteur == 0) {
        printf("Échec de la lecture. Vérifie que le fichier contient bien des lignes au format :\n");
        printf("Nom: XXX, prénom : YYY naissance J-M-A\n");
    }

    fclose(pf);
}


int main()
{
    /*Date D;
    D = CreerDate(13,2,2025);
    afficher_date(D);

    Personne P;
    P = CreerPersonne("sosthene","eddy",D);
    afficher_Personne(P);

    ajouterPfile1(P);
    ajouterPfile2(P);*/

    //demanderUtl1();

    //demanderUtl2();

    recupererEtAfficher10();
    return 0;
}

