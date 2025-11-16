import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

class DecompilerApp:
    def __init__(self, root):
        root.title("Python Bytecode Decompiler")

        self.file_path = None

        self.btn_select = tk.Button(root, text="Select .pyc File", command=self.select_file)
        self.btn_select.pack(pady=5)

        self.lbl_file = tk.Label(root, text="No file selected")
        self.lbl_file.pack()

        self.btn_decompile = tk.Button(root, text="Decompile", command=self.decompile, state="disabled")
        self.btn_decompile.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, width=80, height=25)
        self.text_area.pack(padx=10, pady=10)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("Python bytecode", "*.pyc")])
        if path:
            self.file_path = path
            self.lbl_file.config(text=path)
            self.btn_decompile.config(state="normal")
            self.text_area.delete('1.0', tk.END)
        else:
            self.file_path = None
            self.lbl_file.config(text="No file selected")
            self.btn_decompile.config(state="disabled")

    def decompile(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select a .pyc file first.")
            return

        output_dir = "decompiled_output"
        os.makedirs(output_dir, exist_ok=True)

        try:
            subprocess.run(["uncompyle6", "-o", output_dir, self.file_path], check=True)
            base_name = os.path.basename(self.file_path)
            py_file = os.path.splitext(base_name)[0] + ".py"
            with open(os.path.join(output_dir, py_file), "r", encoding="utf-8") as f:
                code = f.read()

            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, code)

        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Decompilation failed.")
        except FileNotFoundError:
            messagebox.showerror("Error", "uncompyle6 is not installed or not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DecompilerApp(root)
    root.mainloop()
