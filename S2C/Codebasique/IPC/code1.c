#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void handler(int sig) {
    printf("Fils : J'ai reçu le signal !\n");
}

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // Code du fils
        signal(SIGUSR1, handler);
        pause(); // Attend un signal
        exit(0);
    } else {
        // Code du père
        sleep(1); // Laisse le temps au fils de se préparer
        kill(pid, SIGUSR1); // Envoie le signal au fils
        wait(NULL); // Attend la fin du fils
    }
    return 0;
}