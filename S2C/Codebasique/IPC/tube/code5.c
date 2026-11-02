#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>

#define FIFO_NAME "mon_fifo"

int main() {
    // Ouvre le tube nommé en écriture (nécessite que le receveur soit lancé)
    int fd = open(FIFO_NAME, O_WRONLY);
    if (fd == -1) {
        perror("open");
        printf("Erreur : Assurez-vous de lancer d'abord le programme receveur !\n");
        exit(1);
    }
    
    char *msg = "Hello depuis un processus totalement indépendant !";
    write(fd, msg, strlen(msg) + 1);
    printf("Expéditeur : Message envoyé avec succès.\n");
    
    close(fd);
    return 0;
}