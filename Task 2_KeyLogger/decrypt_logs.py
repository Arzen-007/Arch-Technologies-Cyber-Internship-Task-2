from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

PASSWORD = "securepassword123"
LOG_FILE = "keystrokes.enc"
KEY_INFO_FILE = "key_info.bin"
DECRYPTED_LOG_FILE = "decrypted_log.log"

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(password.encode())

def decrypt_logs():
    if not os.path.exists(LOG_FILE) or not os.path.exists(KEY_INFO_FILE):
        print("Required files missing.")
        return

    with open(KEY_INFO_FILE, 'rb') as f:
        key_info = f.read()
        salt, nonce = key_info[:16], key_info[16:]

    key = derive_key(PASSWORD, salt)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()

    with open(LOG_FILE, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    print("Decrypted Logs:\n")
    print(decrypted_data.decode())

    with open(DECRYPTED_LOG_FILE, 'w') as f:
        f.write(decrypted_data.decode())
    print(f"\nSaved to {DECRYPTED_LOG_FILE}")

if __name__ == "__main__":
    decrypt_logs()
