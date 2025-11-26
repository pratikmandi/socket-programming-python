import socket


def start_client():
    host = "localhost"
    port = 8085

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        msg = input("Enter message: ")
        client_socket.send(msg.encode("utf-8"))

        if msg == "exit":
            break

        reply = client_socket.recv(1024).decode("utf-8")
        print("Server:", reply)

    client_socket.close()
    print("Client stopped.")


if __name__ == "__main__":
    start_client()
