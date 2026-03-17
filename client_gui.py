import socket
import threading
import tkinter as tk
from tkinter import simpledialog
import datetime

from crypto_utils import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# -------- GUI --------

window = tk.Tk()
window.withdraw()

username = simpledialog.askstring("Username", "Enter your username")

window.deiconify()
window.title("Encrypted Chat - " + username)

main_frame = tk.Frame(window)
main_frame.pack()

chat_frame = tk.Frame(main_frame)
chat_frame.pack(side=tk.LEFT)

user_frame = tk.Frame(main_frame)
user_frame.pack(side=tk.RIGHT, padx=10)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(
    chat_frame,
    height=20,
    width=60,
    wrap="word",
    yscrollcommand=scrollbar.set
)

chat_box.pack(side=tk.LEFT)

scrollbar.config(command=chat_box.yview)

chat_box.tag_config("self", foreground="green", justify="right")
chat_box.tag_config("other", foreground="blue", justify="left")
chat_box.tag_config("system", foreground="gray", justify="center")

chat_box.config(state=tk.DISABLED)

# -------- Online Users --------

user_label = tk.Label(user_frame, text="Online Users")
user_label.pack()

user_list = tk.Listbox(user_frame, height=20, width=20)
user_list.pack()

# -------- Message Entry --------

message_entry = tk.Entry(window, width=50)
message_entry.pack(side=tk.LEFT, padx=5, pady=5)

message_entry.focus()

# -------- Save Chat --------

def save_chat(message):
    with open("chat_history.txt", "a") as f:
        f.write(message + "\n")

# -------- Receive Messages --------

def receive_messages():

    while True:

        try:

            data = client.recv(4096)

            message = decrypt_message(data)

            chat_box.config(state=tk.NORMAL)

            if "joined the chat" in message:

                user = message.split(" joined")[0]

                if user not in user_list.get(0, tk.END):
                    user_list.insert(tk.END, user)

                chat_box.insert(tk.END, message + "\n", "system")

            else:

                sender = message.split("] ")[1].split(":")[0]

                if sender == username:
                    chat_box.insert(tk.END, message + "\n", "self")
                else:
                    chat_box.insert(tk.END, message + "\n", "other")

            chat_box.config(state=tk.DISABLED)

            chat_box.see(tk.END)

            save_chat(message)

        except:
            break

# -------- Send Message --------

def send_message():

    message = message_entry.get()

    if message == "":
        return

    time = datetime.datetime.now().strftime("%H:%M")

    full_message = f"[{time}] {username}: {message}"

    encrypted = encrypt_message(full_message)

    client.send(encrypted)

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(tk.END, full_message + "\n", "self")

    chat_box.config(state=tk.DISABLED)

    chat_box.see(tk.END)

    save_chat(full_message)

    message_entry.delete(0, tk.END)

# -------- Send Button --------

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

message_entry.bind("<Return>", lambda event: send_message())

# -------- Start Receiving Thread --------

thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

# -------- Notify Join --------

join_message = f"{username} joined the chat"

client.send(encrypt_message(join_message))

window.mainloop()