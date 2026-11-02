#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pid_t pid;
    char buffer[100];

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(1);
    } else if (pid == 0) {
        // Code du fils : attend 3 secondes avant d'écrire
        close(fd[0]);
        printf("Fils : Je dors 3 secondes avant d'écrire dans le tube...\n");
        sleep(3);
        char *msg = "Données envoyées après délai";
        write(fd[1], msg, sizeof(msg));
        close(fd[1]);
        printf("Fils : Données envoyées.\n");
        exit(0);
    } else {
        // Code du père : essaie de lire immédiatement (va se bloquer)
        close(fd[1]);
        printf("Père : Tentative de lecture (va se bloquer en attendant le fils)...\n");
        read(fd[0], buffer, sizeof(buffer));
        printf("Père : Lecture réussie ! Message reçu : '%s'\n", buffer);
        close(fd[0]);
        wait(NULL);
    }
    return 0;
}