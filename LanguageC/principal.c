#include <stdio.h>

int main(int argc, char **argv, char **env){
    printf("Le programme a recu %d parametre(s)\n",argc);

    int i;
    for ( i = 0; i < argc; i++)
    {
        printf("Argument %d = %s\n",i,argv[i]);
    }

    i = 0;
    printf("Affichage des variables d'environnement\n");
    while (env[i])
    {
        printf("env[%d] = %s\n",i,env[i]);
        i = i+1;
    }
    
    return 0;
}