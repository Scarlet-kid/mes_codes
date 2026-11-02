#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        return 1;
    } else if (pid == 0) {
        printf("Fils : PID = %d, PID père = %d\n", getpid(), getppid());
    } else {
        printf("Père : PID = %d, a créé le fils PID = %d\n", getpid(), pid);
        wait(NULL);
    }
    return 0;
}