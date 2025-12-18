import json
"""while True:
    try:
        prixHT = int(input("Entrez le prix hors taxe:"))
        prixTTC = prixHT + prixHT * 0.2
        print(prixTTC)
        break
    except ValueError: # Erreur de type
        print("Attention tu dois entrer un nombre")"""

class FileNotJsonFormatError(Exception):
    def __init__(self):
        self.message = 'Vous ne pouvez mettre que des fichiers en .json'

def read_json_file(file_name):
    try:
        if not file_name.endswith('.json'):
            raise FileNotJsonFormatError
        fichier = open(file_name)
        print(json.load(fichier))
        #print(fichier.readlines())
        fichier.close()
    except FileNotJsonFormatError as e:
        print(e.message)
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    #except IndexError:
        #print("LA ligne que tu veux afficher n'existe pas")
    """finally:
        print("fini")"""

read_json_file('data.json')