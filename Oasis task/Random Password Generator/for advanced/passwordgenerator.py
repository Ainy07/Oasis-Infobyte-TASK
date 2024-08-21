import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character types selected")

    return ''.join(random.choice(character_set) for _ in range(length))

def on_generate():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_copy():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

app = tk.Tk()
app.title("Password Generator")

tk.Label(app, text="Password Length:").pack()
length_entry = tk.Entry(app)
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var).pack()

tk.Button(app, text="Generate", command=on_generate).pack()
tk.Label(app, text="Generated Password:").pack()
password_entry = tk.Entry(app, width=50)
password_entry.pack()

tk.Button(app, text="Copy to Clipboard", command=on_copy).pack()

app.mainloop()
