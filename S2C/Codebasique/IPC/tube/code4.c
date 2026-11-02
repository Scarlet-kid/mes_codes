#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>

#define FIFO_NAME "mon_fifo"

int main() {
    char buffer[100];
    
    // Création du tube nommé (FIFO) s'il n'existe pas
    mkfifo(FIFO_NAME, 0666);

    printf("Receveur : En attente de message sur le tube nommé...\n");
    int fd = open(FIFO_NAME, O_RDONLY);
    read(fd, buffer, sizeof(buffer));
    printf("Receveur : Message reçu d'un processus externe : '%s'\n", buffer);
    close(fd);

    // Suppression du tube nommé à la fin
    unlink(FIFO_NAME);
    return 0;
}