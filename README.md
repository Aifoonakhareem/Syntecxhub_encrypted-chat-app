# 🔐 Encrypted Chat Application

A secure multi-client chat application developed in Python that ensures confidential communication using AES encryption over TCP sockets.

---

## 🚀 Features

* 🔒 End-to-End Encryption using AES
* 🔑 Secure key exchange mechanism
* 💬 Real-time messaging with TCP sockets
* 👥 Multi-client support using threading
* 🖥️ GUI-based chat interface (Tkinter)
* 📜 Chat logging system
* 🛡️ Secure IV handling for encryption

---

## 🏗️ Technologies Used

* Python
* Socket Programming (TCP)
* Cryptography (AES)
* Tkinter (GUI)
* Threading

---

## 📂 Project Structure

* `server.py` – Handles multiple clients and broadcasting
* `client.py` – Terminal-based client
* `client_gui.py` – GUI-based client
* `crypto_utils.py` – Encryption & decryption logic
* `dh_key_exchange.py` – Key exchange logic

---

## ▶️ How to Run

### 1. Start Server

```bash
python server.py
```

### 2. Start Clients

```bash
python client_gui.py
```

### 3. Enter username and chat securely

---

## 🔐 Security Concepts

* AES Encryption for confidentiality
* Secure key exchange
* Initialization Vector (IV) usage
* Multi-client secure communication

---

## 👩‍💻 Author
**Aifoona Khareem**
