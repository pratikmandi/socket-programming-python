import socket


def main():
    host = "127.0.0.1"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print(f"UDP Server started at {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode()

        print(f"From {addr}: {message}")

        if message == "exit":
            print("Client exited. Stopping server.")
            break

    server.close()
    print("Server closed.")


if __name__ == "__main__":
    main()
