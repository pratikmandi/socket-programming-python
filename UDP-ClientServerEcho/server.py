import socket


def main():
    host = "localhost"
    port = 8055

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Echo Server running on {host}:{port}")

    while True:
        message, addr = server_socket.recvfrom(1024)
        print(f"message from client: ", message.decode("utf-8"))

        server_socket.sendto(message, addr)


if __name__ == "__main__":
    main()
