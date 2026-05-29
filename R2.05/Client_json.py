import socket
import json

# Configuration du client
host = "127.0.0.1"  # Adresse IP du serveur
port = 65432        # Port de communication

# Création du socket client et connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Boucle de discussion
while True:
    # Saisir un message et envoyer en format JSON
    client_message = input("Vous (Client) : ")
    message_json = json.dumps({"message": client_message})
    client_socket.send(message_json.encode())
    
    # Vérifier si le client souhaite terminer
    if client_message.lower() == "fin":
        print("Conversation terminée par le client.")
        break

    # Recevoir la réponse du serveur (format JSON)
    data = client_socket.recv(1024).decode()
    server_response = json.loads(data)  # Décoder le message JSON
    print(f"Serveur : {server_response['message']}")
    
    # Vérifier si le serveur souhaite terminer
    if server_response['message'].lower() == "fin":
        print("Conversation terminée par le serveur.")
        break

# Fermeture de la connexion
client_socket.close()