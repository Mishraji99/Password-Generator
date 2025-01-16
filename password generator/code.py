import random
import string

from cryptography.fernet import Fernet;

# Generate a key for encryption (do this once and save the key securely)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
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

# Save password securely
def save_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())

    with open("passwords.txt", "ab") as file:
        file.write(encrypted_password + b'\n')

# Main function to generate, check, and save password
def main():
    # Ensure the key exists
    try:
        load_key()
    except FileNotFoundError:
        generate_key()

    # Generate a password
    password = generate_password()
    print("Generated Password:", password)

    # Check strength
    strength = check_password_strength(password)
    print("Password Strength:", strength)

    # Save the password securely
    save_password(password)
    print("Password saved securely!")

if __name__ == "__main__":
    main()

# Encryption key file (generated once)key.key
# File where encrypted passwords are stored passwords.text