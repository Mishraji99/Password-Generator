import random
import string
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox

# Generate a key for encryption (do this once and save the key securely)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    if not os.path.exists("key.key"):
        raise FileNotFoundError("The encryption key file 'key.key' is missing. Please generate a key first.")
    
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Password strength checker
def check_password_strength(password):
    length = len(password) >= 14
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)

    strength = sum([length, upper, lower, digit, special])
    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Moderate"
    else:
        return "Weak"

# Generate a strong password
def generate_password(length=14):
    if length < 14:
        raise ValueError("Password length must be at least 14 characters for strong security.")

    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Save password securely (encrypt and store it)
def save_password(password):
    try:
        key = load_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())

        with open("passwords.txt", "ab") as file:
            file.write(encrypted_password + b'\n')
        messagebox.showinfo("Success", "Password saved securely!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Encryption key not found. Please generate the encryption key first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the password: {e}")

# Function to handle password generation and strength checking
def generate_and_check_password():
    password = generate_password()  # Generate password
    strength = check_password_strength(password)  # Check password strength
    
    # Display generated password and its strength in the UI
    password_label.config(text=password)
    strength_label.config(text=strength)
    
    # Optionally save the password to file
    save_password(password)

# Setting up the UI with Tkinter
def setup_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Password Generator Tool")
    root.geometry("400x300")
    root.configure(bg="black")
    
    # Add a title label
    title_label = tk.Label(root, text="Generate Password", font=("Arial", 16), bg="lightgray", fg="black")
    title_label.pack(pady=20)
    
    # Add a button to generate password
    generate_button = tk.Button(root, text="Click", font=("Arial", 12), bg="blue", fg="white", command=generate_and_check_password)
    generate_button.pack(pady=10)
    
    # Add a label to display the password
    global password_label
    password_label = tk.Label(root, text="Password Will be Generated Here", font=("Arial", 12), bg="black", fg="white", width=40, height=2)
    password_label.pack(pady=10)
    
    # Add a label to display the password strength
    global strength_label
    strength_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white")
    strength_label.pack(pady=5)
    
    # Start the Tkinter main loop
    root.mainloop()

# Main function to ensure key exists and start the UI
def main():
    # Ensure the key exists
    try:
        load_key()
    except FileNotFoundError:
        messagebox.showwarning("Key Missing", "Encryption key not found. Generating a new key...")
        generate_key()
    
    # Setup and run the UI
    setup_ui()

if __name__ == "__main__":
    main()
