#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t f1 = fork();

    if (f1 == 0) {
        printf("Fils 1 : PID = %d, Père = %d\n", getpid(), getppid());
    } else {
        pid_t f2 = fork();
        if (f2 == 0) {
            printf("Fils 2 : PID = %d, Père = %d\n", getpid(), getppid());
        } else {
            printf("Père : PID = %d\n", getpid());
            wait(NULL);
            wait(NULL);
        }
    }
    return 0;
}

