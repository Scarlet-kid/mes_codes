#include <stdio.h>
#include <stdlib.h>

int* concatene(int tab1[], int size1, int tab2[], int size2) {
    int *tab3;
    tab3 = malloc((size1 + size2) * sizeof(int));
    
    if (tab3 == NULL) return NULL;

    int i = 0;
    // On copie le premier tableau
    for (int j = 0; j < size1; j++, i++) {
        tab3[i] = tab1[j];
    }
    
    // On copie le deuxième tableau
    for (int j = 0; j < size2; j++, i++) {
        tab3[i] = tab2[j];
    }

    return tab3;
}

int main() {
    int tab1[3] = {1, 2, 3};
    int tab2[4] = {4, 5, 6, 7};

    // On récupère le pointeur renvoyé par la fonction
    int *resultat = concatene(tab1, 3, tab2, 4);

    if (resultat != NULL) {
        // Affichage pour vérifier
        for (int i = 0; i < 7; i++) {
            printf("%d ", resultat[i]);
        }
        printf("\n");

        // Très important : on libère la mémoire allouée par malloc
        free(resultat);
    }

    return 0;
}