import tkinter as tk
from tkinter import messagebox
import sqlite3

def validate_username(username):
    return "@" in username

def validate_password(password, password2):
    return password == password2

def create_account():
    username = username_entry.get()
    password = password_entry.get()
    password2 = confirm_password_entry.get()

    if not validate_username(username):
        messagebox.showerror("Error", "Username must contain '@' symbol.")
        return

    if not validate_password(password, password2):
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    # Save to database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Account created successfully!")

# GUI
root = tk.Tk()
root.title("Sign Up")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()

confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

sign_up_button = tk.Button(root, text="Sign Up", command=create_account)
sign_up_button.pack()

root.mainloop()
