# Password Generator with Strength Checker and Encrypted Storage

## Overview
The **Password Generator with Strength Checker and Encrypted Storage** is a Python-based tool designed to generate secure passwords, evaluate their strength, and store them securely using encryption. It ensures that passwords meet strong security standards by checking for length, uppercase, lowercase, digits, and special characters. The tool then encrypts the passwords using the **cryptography.fernet** module before saving them in a file for safe storage.

## Features
- **Password Generation**: Generates random, secure passwords with a minimum length of 14 characters.
- **Password Strength Checker**: Checks password strength based on length, character variety, and complexity.
- **Encrypted Storage**: Saves encrypted passwords securely using **Fernet encryption**.
- **Key Management**: Generates and stores an encryption key for secure password handling.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Password-Generator-With-Encryption.git
    ```
2. Install dependencies:
    ```bash
    pip install cryptography
    ```

## Usage
1. Run the Python script:
    ```bash
    python code.py
    ```
2. The script will generate a password, check its strength, and display the results.
3. The generated password will be encrypted and saved in `passwords.txt`.

## File Structure


## Technologies Used
- **Python**: For password generation, strength checking, and encryption.
- **cryptography**: For password encryption using **Fernet**.

## License
This project is open-source and available under the MIT License.
