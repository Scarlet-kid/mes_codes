#include <stdio.h>

int fibo(int n)
{
    if(n==0 || n==1)
    {
        return n;
    }
    else
    {
        return fibo(n-1) + fibo(n-2);
    }
}

void trier(int tab[], int n)
{
    int i;
    int j;
    int tmp;
    for(i=1;i<=n;i++)
    {
        tmp = tab[i];
        j = i;
        while (j>0 && tab[j-1]>tmp)
        {
            tab[j] = tab[j-1];
            j --;
        }
        tab[j] = tmp;
    }
}

void afficher(int tab[], int n)
{
    printf("[");
    for(int i = 0; i<n; i++)
    {
        printf("%d",tab[i]);
        if(i < n-1)
        {
            printf(", ");
        }
    }
    printf("]");
}

int main()
{
    int tab[5] = {2,4,1,0,8};
    afficher(tab,5);
    trier(tab,5);
    afficher(tab,5);
    printf("\n");
    return 0;
}
