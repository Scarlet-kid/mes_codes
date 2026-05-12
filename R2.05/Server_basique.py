import socket

host = "127.0.0.1"  
port = 1337        

server_socket = socket.socket()#socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Serveur en attente de connexion...")
conn, addr = server_socket.accept()
print(f"Connexion établie avec {addr}")

while True:
    # Recevoir le message du client
    client_message = conn.recv(1024).decode()
    print(f"Client : {client_message}")
    if client_message.lower() == "fin":
        print("Conversation terminée par le client.")
        break
    server_message = input("Vous (Serveur) : ")
    conn.send(server_message.encode())
    if server_message.lower() == "fin":
        print("Conversation terminée par le serveur.")
        break

conn.close()
server_socket.close()