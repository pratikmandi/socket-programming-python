import threading
import socket

host = "localhost"
port = 8788
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"Server started at {host}:{port}")


clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.pop(index)
            client.close()
            nickname = nicknames[index]
            print(f"{nickname} has left the chat!")
            nicknames.pop(nickname)
            break


def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected to client: {str(address)}")
        client.send("CONNECTION_TOKEN".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!\n".encode("ascii"))
        client.send(f"Connected to the server".encode("ascii"))

        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()


recieve()
