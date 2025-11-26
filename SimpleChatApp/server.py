import socket


def start_server():
    host = "localhost"
    port = 8085

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started at {host}:{port}, waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        msg = conn.recv(1024).decode("utf-8")

        if not msg:
            print("Client disconnected.")
            break

        if msg == "exit":
            print("Client requested exit. Closing...")
            break

        print("Client:", msg)

        reply = input("Enter message: ")
        conn.send(reply.encode("utf-8"))

    conn.close()
    server_socket.close()
    print("Server stopped.")


if __name__ == "__main__":
    start_server()
