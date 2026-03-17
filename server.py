import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []
public_keys = {}


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)


def handle_client(client):

    while True:
        try:
            data = client.recv(4096)

            if not data:
                break

            broadcast(data, client)

        except:
            clients.remove(client)
            client.close()
            break


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen()

    print("Server started...")

    while True:

        client, addr = server.accept()

        print("Connected:", addr)

        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


start_server()