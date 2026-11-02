#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pid_t pid;
    char buffer[100];
    char *msg = "Bonjour papa depuis le fils !";

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(1);
    } else if (pid == 0) {
        // Code du fils (écrivain)
        close(fd[0]); // Ferme l'extrémité de lecture non utilisée
        write(fd[1], msg, strlen(msg) + 1);
        close(fd[1]);
        exit(0);
    } else {
        // Code du père (lecteur)
        close(fd[1]); // Ferme l'extrémité d'écriture non utilisée
        read(fd[0], buffer, sizeof(buffer));
        printf("Père : J'ai reçu le message : '%s'\n", buffer);
        close(fd[0]);
        wait(NULL);
    }
    return 0;
}