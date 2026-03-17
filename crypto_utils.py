from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import hmac

KEY = hashlib.sha256(b"shared_secret_key").digest()

def encrypt_message(message):
    iv = get_random_bytes(16)

    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)
    ciphertext = cipher.encrypt(message.encode())

    mac = hmac.new(KEY, ciphertext, hashlib.sha256).digest()

    return iv + ciphertext + mac


def decrypt_message(data):

    iv = data[:16]
    mac = data[-32:]
    ciphertext = data[16:-32]

    expected_mac = hmac.new(KEY, ciphertext, hashlib.sha256).digest()

    if not hmac.compare_digest(mac, expected_mac):
        raise ValueError("Message integrity failed")

    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)

    return cipher.decrypt(ciphertext).decode()