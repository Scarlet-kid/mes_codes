import socket
import random
import threading
import time

def gerer_jeu_client(client, address):
    
    print(f"\n[+] Nouveau joueur connecté depuis {address}")
    
    try:
        # Envoi de la bannière de bienvenue
        banniere = "\n===================\nBienvenue dans ce jeu\nVeuillez donner un nombre maximum pour le tirage aleatoire\nBonne chance\n===================\n\n"
        client.send(banniere.encode("utf8"))
        
        n = client.recv(8).decode("utf8").strip()
        nbr = int(n)
        print(f"[{address}] Le nombre maximum choisi est : {nbr}")
        
        alea = random.randint(1, nbr)
        
        while True:
            # Attente de la proposition du joueur
            nbr_c = client.recv(10).decode("utf8").strip()
            
            if not nbr_c: # Si le client se déconnecte brutalement
                break
                
            print(f"[{address}] Proposition reçue : {nbr_c}")
            proposition = int(nbr_c)
            
            if proposition == alea:
                client.send("fini".encode("utf8"))

                time.sleep(0.5) 
                client.send("vous avez trouve\n".encode("utf8"))
                break
                
            elif proposition < alea:
                client.send("plus".encode("utf8"))
            else:
                client.send("moins".encode("utf8"))
                
    except Exception as e:
         print(f"[-] Une erreur est survenue avec {address} : {e}")
         
    finally:
        print(f"[-] Fin de partie. Fermeture de la connexion pour {address}")
        client.close()

#Configuration du Serveur Principal
host = "127.0.0.1"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5) # On autorise jusqu'à 5 clients en file d'attente

print(f"Serveur de jeu en écoute sur le port {port}...")

# La boucle infinie qui accepte les clients
while True:
    client, address = s.accept()
    
    # Délégation de la partie à un nouveau thread
    thread_client = threading.Thread(target=gerer_jeu_client, args=(client, address))
    thread_client.start()