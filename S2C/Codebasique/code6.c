#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        int a = 2, b = 3;
        int res = a + b;
        exit(res); // Le code de sortie est codé sur 8 bits (0-255)
    } else {
        int status;
        wait(&status);
        if (WIFEXITED(status)) {
            printf("Père : le fils a calculé 2 + 3 = %d\n", WEXITSTATUS(status));
        }
    }
    return 0;
}