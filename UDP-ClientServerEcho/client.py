import socket


def main():
    host = "localhost"
    port = 8055

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message: ")

        if message.lower() == "exit":
            break

        client_socket.sendto(message.encode(), (host, port))

        data, _ = client_socket.recvfrom(1024)
        print("From server: ", data.decode())

    client_socket.close()


if __name__ == "__main__":
    main()
