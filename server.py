import socket
import threading

ip = socket.gethostbyname(socket.gethostname())
port = 8888
size_msg = 1024
form = "utf-8"

def handle_client(conn, addr):
    print(f"connection: {ip}:{port} connected.")

    connected = True
    while connected:
        msg = conn.recv(size_msg).decode(form)
        if msg == "!DC":
            connected = False

        print(f"{ip}:{port}: {msg}")
        msg = f"Msg received: {msg}"
        conn.send(msg.encode(form))

    conn.close()

def main():
    print("Start...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    print(f"listen: {ip}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"number connections: {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
