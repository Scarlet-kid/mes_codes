import socket, time

host="127.0.0.1"
port = 1337
s=socket.socket()
s.connect((host,port))
data=s.recv(1024)
print(data.decode())
nbr0=input()
s.send(nbr0.encode("utf8"))
reponse="test"
point=0
while ( True ):
    if (reponse!="fini"):
        nbr=int(input("entrez un nombre\n"))
        s.send(str(nbr).encode("utf8"))
        reponse=s.recv(10)
        reponse=reponse.decode("utf8")
        print(reponse)
        point=point+1
    else:
        print("c'est fini")
        print("vous avez gagné en ",point," coups")
        break
s.close()
