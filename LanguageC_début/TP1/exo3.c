#include <stdio.h>

int chaineVersEntier(char c) {
    return c - '0'; 
}

int tableauVersEntier(char *tab) {
    int resultat = 0;
    for (int i = 0; i < 4; i = i + 1) {
        int valeurChiffre = chaineVersEntier(tab[i]);
        resultat = resultat * 10 + valeurChiffre;
    }
    return resultat;
}

int main() {
    char monTableau[4] = {'1', '9', '8', '4'};
    int resultat = tableauVersEntier(monTableau);
    printf("Le tableau ['1','9','8','4'] devient l'entier : %d\n", resultat);
    return 0;
}