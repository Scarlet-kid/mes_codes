import socket
import threading
import json

def gerer_client(conn, addr):
    """
    Fonction exécutée par un thread distinct pour chaque client.
    """
    # Le serveur affiche l'adresse IP et le port du client connecté
    print(f"\n[+] Nouvelle connexion établie avec l'adresse IP {addr[0]} sur le port {addr[1]}")
    
    # Le serveur envoie une bannière au client
    banniere = {"message": "bonjour, je suis le serveur"}
    conn.send(json.dumps(banniere).encode())
    
    while True:
        try:
            # Le serveur attend que le client envoie des données
            data = conn.recv(1024).decode()
            if not data:
                break
            
            client_message = json.loads(data)
            texte_recu = client_message.get('message', '')
            print(f"[{addr[0]}:{addr[1]}] Client : {texte_recu}")
            
            # Si le client envoie "exit", on ferme la connexion proprement
            if texte_recu.lower() == "exit":
                print(f"[-] {addr[0]}:{addr[1]} a demandé la déconnexion.")
                break
            
            # Après réception, le serveur répond automatiquement
            reponse = {"message": "données bien reçues"}
            conn.send(json.dumps(reponse).encode())
            
        except (ConnectionResetError, json.JSONDecodeError):
            print(f"[-] Erreur ou déconnexion inattendue avec {addr}")
            break

    # Fermeture de la connexion proprement pour ce client
    conn.close()

# Configuration du serveur
host = "127.0.0.1"
port = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Option pour permettre de réutiliser le port immédiatement si on relance le script
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((host, port))
server_socket.listen(5) # Permet de mettre en attente jusqu'à 5 connexions simultanées
print(f"Serveur en écoute sur {host}:{port}...")

# Boucle principale : accepte les connexions et crée un thread par client
while True:
    conn, addr = server_socket.accept()
    
    # Crée un serveur Python qui autorise la connexion de plusieurs clients en utilisant des threads
    client_thread = threading.Thread(target=gerer_client, args=(conn, addr))
    client_thread.start()