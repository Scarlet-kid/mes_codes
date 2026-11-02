#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pid_t pid;
    pid_t child_pid_received;

    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(1);
    } else if (pid == 0) {
        // Code du fils
        close(fd[0]); // Ferme la lecture
        pid_t my_pid = getpid();
        write(fd[1], &my_pid, sizeof(my_pid)); // Envoie son propre PID
        close(fd[1]);
        exit(0);
    } else {
        // Code du père
        close(fd[1]); // Ferme l'écriture
        read(fd[0], &child_pid_received, sizeof(child_pid_received));
        printf("Père : Le PID de mon fils reçu via le tube est %d\n", child_pid_received);
        close(fd[0]);
        wait(NULL);
    }
    return 0;
}