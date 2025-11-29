import socket
import threading
import queue

CMD_QUEUE = queue.Queue()

def command_input_thread():
    while True:
        cmd = input("Enter command for client: ")
        CMD_QUEUE.put(cmd)
        if cmd.lower() == "exit":
            break


def main():
    host = "127.0.0.1"
    port = 6000

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((host, port))

    print(f"[SERVER] Command server running at {host}:{port}")

    # Start thread for manual command input
    threading.Thread(target=command_input_thread, daemon=True).start()

    client_addr = None

    while True:
        data, addr = server_sock.recvfrom(1024)
        msg = data.decode()

        if msg == "HEARTBEAT":
            client_addr = addr
            print(f"[SERVER] Heartbeat received from {addr}")

            # Send queued command if available
            if not CMD_QUEUE.empty():
                cmd = CMD_QUEUE.get()
                print(f"[SERVER] Sending command: {cmd}")
                server_sock.sendto(cmd.encode(), client_addr)

                if cmd.lower() == "exit":
                    print("[SERVER] Exit command sent. Stopping server.")
                    break
            else:
                # No command → send NOOP
                server_sock.sendto("NOOP".encode(), client_addr)

    server_sock.close()


if __name__ == "__main__":
    main()
