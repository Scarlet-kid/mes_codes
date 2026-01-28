#include <stdio.h>

int main()
{
    char op ;
    int n1, n2 ;
    printf("operation souhaitee (+ ou *) ? ");
    scanf("%c",&op) ;
    printf("Donnez 2 nombres entiers : ");
    scanf("%d %d",&n1,&n2);
    if (op == '+')
    {
        printf ("leur somme est %d",n1+n2);
    } 
    else
    {
        printf("leur produit est : %d\n",n1*n2);
    }
    return 0;
}
