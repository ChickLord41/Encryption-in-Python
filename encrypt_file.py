from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Path to the file to encrypt
file_path = "example.txt"

with open(file_path, "rb") as file:
    original = file.read()

# Encrypt
encrypted = fernet.encrypt(original)

# Save the encrypted data
with open(file_path + ".encrypted", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print(f"{file_path} encrypted successfully.")
