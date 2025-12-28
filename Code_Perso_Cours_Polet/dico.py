def moyenne(listeNotes: list) -> float:
    somme: float
    somme = 0
    for note in listeNotes:  # le for __ in __ peut calculer des sommes suffit juste que les élements soient de type int.
        somme = somme + note
    return somme / len(listeNotes)


def moyenneEtu(etudiant: dict) -> None:
    etudiant['moyenne'] = moyenne(etudiant['notes'])


def moyennePromo(lesEtudiants: list) -> float:
    somme: float = 0
    nbEtu = 0
    try:
        for etu in lesEtudiants:
            if not 'moyenne' in etu:
                raise Exception("pas de moyenne!!!")
            somme = somme + etu['moyenne']
            nbEtu = nbEtu + 1
        return somme / nbEtu

    except Exception as error:
        print("error-->",error)
        print('calcul des moyennes manquantes...')
        for etu in lesEtudiants:
            if not 'moyenne' in etu:
                print('traitement de :',etu['nom'])
                moyenneEtu(etu)

        return moyennePromo(lesEtudiants)


def prog():
    roger = {'nom': 'Roulemapoule', 'prenom': 'Roger', 'notes': [3, 7, 12, 15]}
    moyenneEtu(roger)
    print("moyenne de Roger:", roger['moyenne'])

    albert = {'nom': 'Alassoupe', 'prenom': 'Albert', 'notes': [3, 7, 12, 15]}
    bernard = {'nom': 'Biengentil', 'prenom': 'Bernard', 'notes': [9, 9.5, 12.5, 11.5]}
    promo = [albert, bernard, roger]

    print('moyenne de la promo :', moyennePromo(promo))


if __name__ == "__main__":
    prog()
