import random

P = 23
G = 5

def generate_private_key():
    return random.randint(1, 100)

def generate_public_key(private_key):
    return pow(G, private_key, P)

def generate_shared_key(public_key, private_key):
    return pow(public_key, private_key, P)