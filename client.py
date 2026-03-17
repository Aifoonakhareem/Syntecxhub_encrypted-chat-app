import socket
import threading
from crypto_utils import encrypt_message, decrypt_message
from dh_key_exchange import *

HOST = '127.0.0.1'
PORT = 5000

username = input("Enter your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            encrypted = client.recv(1024)
            message = decrypt_message(encrypted)
            print(message)
        except:
            break

def send():
    while True:
        message = input("")
        full_message = username + ": " + message
        encrypted = encrypt_message(full_message)
        client.send(encrypted)

threading.Thread(target=receive).start()
threading.Thread(target=send).start()