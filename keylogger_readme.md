# 🔐 Advanced Python Keylogger Tool

A secure, cross-platform Python keylogger with AES encryption, GUI-based log viewer, and standard-compliant code for ethical usage, research, and testing.

---

## 📁 Project Structure

```
keylogger/
├── encrypted_keylogger.py       # Main encrypted keylogger script
├── decrypt_logs.py              # Decrypts keystroke logs
├── keylog_viewer_gui.py         # GUI viewer for decrypted logs
└── keylogger_env/               # Python virtual environment (excluded from repo)
```

---

## 📌 Features

- ✅ AES-encrypted keystroke logging
- ✅ Timestamped logs for detailed session tracking
- ✅ Safe and structured decryption using PBKDF2
- ✅ GUI-based log viewer (Tkinter-powered)
- ✅ Works on Linux, macOS, and Windows (multi-platform support)
- ✅ Secure coding practices and modular code

---

## ⚙️ Setup Instructions (Kali Linux)

### 1. 🔧 Create a Virtual Environment

```bash
cd ~/Desktop
mkdir keylogger && cd keylogger
python3 -m venv keylogger_env
source keylogger_env/bin/activate
```

### 2. 📦 Install Dependencies

```bash
pip install pynput cryptography
```

### 3. 🧪 Create Required Files

Copy the following files into your project folder:

- `encrypted_keylogger.py`
- `decrypt_logs.py`
- `keylog_viewer_gui.py`

---

## 🚀 Usage Guide

### 1. ▶️ Run the Keylogger

```bash
python encrypted_keylogger.py
```

- Press `Esc` to stop logging.
- This creates: `keystrokes.enc`, `key_info.bin`

### 2. 🔓 Decrypt the Logs

```bash
python decrypt_logs.py
```

- Shows output in terminal
- Saves output to: `decrypted_log.log`

### 3. 🖥️ View Logs with GUI

```bash
python keylog_viewer_gui.py
```

- Click **"Open Log File"** and select `decrypted_log.log`

---

## 📄 Requirements

- Python 3.8+
- OS: Linux / macOS / Windows
- Modules:
  - `pynput`
  - `cryptography`
  - `tkinter` (included in Python by default)

---

## 🛡️ Disclaimer

This tool is for **educational** and **ethical research** purposes only. Do **not** use it on systems you do not own or have explicit permission to test.

---

## 📸 Screenshots & Terminal Logs

Refer to the `documentation_report.docx` for full step-by-step command screenshots and outputs.

