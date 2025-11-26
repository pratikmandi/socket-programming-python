import socket


def start_client():
    host = "localhost"
    port = 8055

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Enter message: ")

    while message.lower() != "exit":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(f"From server: {data}")
        message = input("Enter message: ")

    client_socket.close()


if __name__ == "__main__":
    start_client()
