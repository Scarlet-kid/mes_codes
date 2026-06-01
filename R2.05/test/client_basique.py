import socket
host = "127.0.0.1"
port = 1337
client_socket = socket.socket()
client_socket.connect((host,port))

while True:
    client_message = input("Vous client :")
    client_socket.send(client_message.encode())
    if(client_message.lower() == "fin"):
        print("Conversation terminée par le client")
        break
    server_message = client_socket.recv(1024).decode()
    print(f" Serveur : {server_message}")
    if(server_message.lower() == "fin"):
        print("Conversation terminée par le serveur")
        break
client_socket.close()
