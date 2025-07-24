import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def parse_log_line(line):
    parts = line.strip().split(" | ")
    if len(parts) == 2:
        return parts[0], parts[1], ""
    else:
        return [line.strip(), "", ""]

def load_log(file_path):
    entries = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("===="):
                continue
            parsed = parse_log_line(line)
            entries.append(parsed)
    return entries

def open_log():
    file_path = filedialog.askopenfilename(filetypes=[("Log Files", "*.log")])
    if not file_path:
        return
    try:
        logs = load_log(file_path)
        for row in tree.get_children():
            tree.delete(row)
        for log in logs:
            tree.insert("", "end", values=log)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open log file:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Keylogger Log Viewer")
root.geometry("700x400")

columns = ("Timestamp", "Action", "Details")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
open_btn = tk.Button(btn_frame, text="Open Log File", command=open_log)
open_btn.pack()

root.mainloop()
