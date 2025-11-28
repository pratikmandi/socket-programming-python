import threading
import socket

host = "localhost"  # 127.0.0.1
port = 8788

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

nickname = input("Enter nickname: ")


def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")

            if message == "CONNECTION_TOKEN":
                client.send(nickname.encode("ascii"))
            else:
                print(message)

        except:
            print("An error has occured!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
