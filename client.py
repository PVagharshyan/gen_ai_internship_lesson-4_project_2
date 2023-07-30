import socket

ip = socket.gethostbyname(socket.gethostname())
port = 8888
size_msg = 1024
form = "utf-8"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    print(f"Client connected: {ip}:{port}")

    connected = True
    while connected:
        msg = input("msg >>> ")

        client.send(msg.encode(form))

        if msg == "!DC":
            connected = False
        else:
            msg = client.recv(size_msg).decode(form)
            print(f"server: {msg}")

if __name__ == "__main__":
    main()

