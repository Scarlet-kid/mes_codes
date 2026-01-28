#include <stdio.h>

void inverser_valeur(int *nb1,int *nb2)
{
    int temp = 0;
    temp = *nb1;
    *nb1 = *nb2;
    *nb2 = temp;
}

int main()
{
    int nb1 = 18;
    int nb2 = 25;

    printf("Avant modification nb1=%d et nb2=%d\n",nb1,nb2);
    inverser_valeur(&nb1, &nb2);
    printf("Après modification nb1=%d et nb2=%d\n",nb1,nb2);
    
    return 0;
}