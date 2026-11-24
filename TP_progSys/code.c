#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <stdlib.h>
#include <time.h>

int choix_joueur_1 = 0;
int choix_joueur_2 = 0;
int nb_signaux_recus = 0;
int signal_recu_joueur = 0;

void handler_arbitre(int sig)
{
    if (nb_signaux_recus == 0) {
        choix_joueur_1 = sig;
        nb_signaux_recus = 1;
    } else if (nb_signaux_recus == 1) {
        choix_joueur_2 = sig;
        nb_signaux_recus = 2;
    }
}

void handler_joueur(int sig)
{
    signal_recu_joueur = sig;
}

int tirer_coup(const char *nom_joueur)
{
    srand(time(NULL) ^ getpid());
    int tirage = rand() % 3;

    if (tirage == 0) {
        printf("%s joue Feuille (SIGUSR1)\n", nom_joueur);
        return SIGUSR1;
    } else if (tirage == 1) {
        printf("%s joue Pierre (SIGUSR2)\n", nom_joueur);
        return SIGUSR2;
    } else {
        printf("%s joue Ciseaux (SIGINT)\n", nom_joueur);
        return SIGINT;
    }
}

void executer_joueur(const char *nom_joueur)
{
    signal(SIGUSR1, handler_joueur);
    signal(SIGUSR2, handler_joueur);
    signal(SIGINT, handler_joueur);

    pause();

    int coup = tirer_coup(nom_joueur);
    kill(getppid(), coup);

    pause();

    if (signal_recu_joueur == SIGUSR1) {
        printf("%s : J'ai GAGNE !\n", nom_joueur);
    } else if (signal_recu_joueur == SIGUSR2) {
        printf("%s : J'ai PERDU !\n", nom_joueur);
    } else if (signal_recu_joueur == SIGINT) {
        printf("%s : EGALITE !\n", nom_joueur);
    }
}

int main(void)
{
    signal(SIGUSR1, handler_arbitre);
    signal(SIGUSR2, handler_arbitre);
    signal(SIGINT, handler_arbitre);

    pid_t pid1 = fork();
    if (pid1 == -1) {
        perror("Erreur fork 1");
        return 1;
    }
    if (pid1 == 0) {
        executer_joueur("Joueur 1");
        return 0;
    }

    pid_t pid2 = fork();
    if (pid2 == -1) {
        perror("Erreur fork 2");
        return 1;
    }
    if (pid2 == 0) {
        executer_joueur("Joueur 2");
        return 0;
    }

    usleep(100000);

    printf("Arbitre : Top depart pour Joueur 1 !\n");
    kill(pid1, SIGUSR1);
    pause();

    printf("Arbitre : Top depart pour Joueur 2 !\n");
    kill(pid2, SIGUSR1);
    pause();

    usleep(100000);

    if (choix_joueur_1 == choix_joueur_2) {
        printf("Arbitre : Egalite !\n");
        kill(pid1, SIGINT);
        kill(pid2, SIGINT);
    } else if ((choix_joueur_1 == SIGUSR1 && choix_joueur_2 == SIGUSR2) ||
               (choix_joueur_1 == SIGUSR2 && choix_joueur_2 == SIGINT)  ||
               (choix_joueur_1 == SIGINT  && choix_joueur_2 == SIGUSR1)) {
        printf("Arbitre : Joueur 1 gagne !\n");
        kill(pid1, SIGUSR1);
        kill(pid2, SIGUSR2);
    } else {
        printf("Arbitre : Joueur 2 gagne !\n");
        kill(pid1, SIGUSR2);
        kill(pid2, SIGUSR1);
    }

    wait(NULL);
    wait(NULL);

    return 0;
}