from cryptography.fernet import Fernet
import os


def load_key():
    return open("secret.key", "rb").read()


def decrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as f:
        f.write(decrypted_data)

def find_files(directory):
    file_list = []

    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)

            # Ignore key file
            if not name.endswith(".key") and name not in ("ransomware.py", "decrypt.py"):
                file_list.append(path)

    return file_list

def main():
    key = load_key()
    files = find_files("ransomware")
    for file in files:
        decrypt_file(file, key)
    print("restored files sucess")

if __name__ == "__main__":
    main()