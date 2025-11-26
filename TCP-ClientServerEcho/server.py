import socket


def start_server():
    host = "localhost"
    port = 8055

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started at {host}:{port}, waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"From client: {data}")
        conn.send(data.encode())

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
