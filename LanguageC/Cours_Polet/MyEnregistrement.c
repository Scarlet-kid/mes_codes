#include <stdio.h>
#include <stdlib.h>


typedef struct 
{
    char *data;
    int date;
    //char evenement;
    int nb_Date;
} DATE;

int demander(DATE d, int nb_de_date)
{
    d.nb_Date = nb_de_date;
    d.data = (char *) malloc(nb_de_date*sizeof(char));

    for(int i=1; i<=nb_de_date; i++)
    {
        char MaDate;
        printf("Date [%d]\n",i);
        printf("Saisir la date (ex:10-12-2025) :");
        scanf("%c",&MaDate);
        d.data[i] = MaDate;
    }
    return 0;
}

void afficherDate(DATE d,int nb_de_date)
{
    d.nb_Date = nb_de_date;
    for(int j=1; j<=d.nb_Date; j++)
    {
        printf("Date numéro[%d] : %c\n",j,d.data[j]);
    }
}

int main()
{
    int nb;
    printf("Nombre de date que vous voulez ajouter :");
    scanf("%d",&nb);
    DATE Mydate;
    demander(Mydate,nb);
    printf("\n");
    afficherDate(Mydate,nb);
    return 0;
}

