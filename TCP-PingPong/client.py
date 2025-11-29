import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9001


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST, SERVER_PORT))

    while True:
        msg = input("You: ").strip()
        s.send(msg.encode())

        if msg.lower() == "exit":
            break

        data = s.recv(1024)
        print("Server:", data.decode().strip())

    s.close()


if __name__ == "__main__":
    main()
