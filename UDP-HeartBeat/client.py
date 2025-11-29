import socket
import threading
import time

running = True  # controls heartbeat thread


def heartbeat(sock, server_addr):
    """Send heartbeat every 5 seconds until stopped."""
    global running
    while running:
        sock.sendto(b"heartbeat", server_addr)
        time.sleep(5)


def main():
    global running

    server_host = "127.0.0.1"
    server_port = 8080
    server_addr = (server_host, server_port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Start heartbeat thread
    th = threading.Thread(target=heartbeat, args=(client, server_addr))
    th.daemon = True
    th.start()

    print("UDP client started. Type messages.")
    print("Type 'exit' to stop client and also stop server.\n")

    while True:
        msg = input("> ")

        if msg == "exit":
            running = False  # stop heartbeat thread
            client.sendto(b"exit", server_addr)
            time.sleep(0.2)  # ensure last message is sent
            client.close()
            print("Client closed. Server will stop too.")
            break

        client.sendto(msg.encode(), server_addr)


if __name__ == "__main__":
    main()
