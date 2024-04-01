import tkinter as tk
from tkinter import messagebox
import sqlite3

def sign_in():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        response_label.config(text="Sign-in successful", fg="green")
    else:
        response_label.config(text="Sign-in unsuccessful", fg="red")

# GUI
root = tk.Tk()
root.title("Sign In")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

sign_in_button = tk.Button(root, text="Sign In", command=sign_in)
sign_in_button.pack()

response_label = tk.Label(root, text="", fg="black")
response_label.pack()

root.mainloop()