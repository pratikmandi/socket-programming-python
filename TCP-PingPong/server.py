import socket
import threading


def handle_client(conn, addr):
    print(f"[SERVER] Connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        msg = data.decode().strip()
        print(f"[SERVER] Received: {msg}")

        if msg.lower() == "ping":
            conn.send(b"pong\n")
        else:
            conn.send(b"unknown\n")

    conn.close()
    print(f"[SERVER] Disconnected: {addr}")


def main():
    host = "127.0.0.1"
    port = 9001

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[SERVER] Listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
