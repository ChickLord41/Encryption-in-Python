from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Path to the encrypted file
encrypted_path = "example.txt.encrypted"

with open(encrypted_path, "rb") as encrypted_file:
    encrypted = encrypted_file.read()

# Decrypt
decrypted = fernet.decrypt(encrypted)

# Save the decrypted file
with open("example_decrypted.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted)

print(f"{encrypted_path} decrypted successfully.")
