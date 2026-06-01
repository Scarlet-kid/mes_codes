import socket
host = "127.0.0.1"
port = 1337
server_socket = socket.socket()
server_socket.bind((port,port))
server_socket.listen(1)
print("Serveur en attente de connexion ...")
conn, adr = server_socket.accept()
print(f"Connexion établie avec {conn}")

while True:
    client_message = conn.recv(1024).decode()
    print(f"Client : {client_message}")
    if client_message.lower() == "fin":
        print("Conversation terminée par le client.")
        break

    server_message = input(" Vous serveur :")
    conn.send(server_message.encode())
    if server_message.lower() == "fin":
        print("Conversation terminée par le serveur")
        break

conn.close()
server_socket.close()