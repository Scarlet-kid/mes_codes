#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void 

int main(void)
{
    pid_t pid = fork();
    if(pid == -1)
    {
        perror("Erreur de fork");
        return 1;
    }

    if(pid == 0)
    {
        // code du joueur 1 uniquement fils
        printf("Je suis le process fils(joueur1), mon pid est %d et celui de mon pere est %d\n",getpid(),getppid());

    }
    else
    {
        printf("Je suis l'arbitre(le père) mon pid est %d et celui de mon fils est %d\n",getpid(),pid);
    }
    return 0;
}