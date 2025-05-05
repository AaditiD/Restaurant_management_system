import tkinter as tk
import re
import subprocess
import sys

# Colors
ORANGE = "#FFA500"
WHITE = "#FFFFFF"
GREY = "#555555"
BG = "#FFF4E6"
ERROR_COLOR = "#FF4C4C"

# Root window setup
root = tk.Tk()
root.title("Login/Register")
root.geometry("400x600")
root.configure(bg=BG)
root.resizable(False, False)

# Container
container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True)

# Switch Function
def show_login():
    register_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_register():
    login_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

# Helper: Entry with Placeholder and Error Label
def create_entry(parent, placeholder, show=None):
    wrapper = tk.Frame(parent, bg=WHITE)
    
    entry_var = tk.StringVar()
    entry = tk.Entry(wrapper, textvariable=entry_var, font=("Segoe UI", 10), fg=GREY, bg=WHITE, bd=0)
    entry.insert(0, placeholder)
    entry.show_char = show  # Save original show value
    entry.placeholder = placeholder

    def on_focus_in(event):
        if entry.get() == entry.placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
            if entry.show_char:
                entry.config(show=entry.show_char)

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, entry.placeholder)
            entry.config(fg=GREY)
            if entry.show_char:
                entry.config(show="")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    entry.pack(fill="x", padx=10, pady=5)
    error_label = tk.Label(wrapper, text="", fg=ERROR_COLOR, bg=WHITE, font=("Segoe UI", 8))
    error_label.pack(padx=10, anchor="w")
    wrapper.pack(fill="x", padx=30, pady=5)
    wrapper.config(highlightbackground=GREY, highlightthickness=1)
    return entry, error_label

# ------------------ Login Frame ------------------
login_frame = tk.Frame(container, bg=BG)

header = tk.Frame(login_frame, bg=ORANGE, height=150)
header.pack(fill="x")
tk.Label(header, text="Login", bg=ORANGE, fg=WHITE, font=("Segoe UI", 20, "bold")).pack(pady=50)

card = tk.Frame(login_frame, bg=WHITE, bd=0)
card.pack(pady=20, padx=20, fill="x")

login_email, login_email_error = create_entry(card, "Email")
login_password, login_password_error = create_entry(card, "Password", show="*")

def validate_login():
    valid = True
    email = login_email.get().strip()
    password = login_password.get().strip()
    login_email_error.config(text="")
    login_password_error.config(text="")

    if email == "Email" or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        login_email_error.config(text="Enter a valid email.")
        valid = False
    if password == "Password" or len(password) < 6:
        login_password_error.config(text="Password must be at least 6 characters.")
        valid = False

    if valid:
        print("Login successful (mock)")
        # Launch restaurant.py
        try:
            # Use subprocess.Popen to run in a new process
            process = subprocess.Popen([sys.executable, "restaurant.py"])
            # Optionally, you can wait for it to finish:
            # process.wait()
            # Or, you can continue without waiting:
        except FileNotFoundError:
            print("Error: restaurant.py not found.  Make sure it's in the same directory.")

tk.Button(card, text="Login", bg=ORANGE, fg=WHITE, font=("Segoe UI", 10, "bold"),
          relief="flat", height=2, command=validate_login).pack(pady=15, padx=30, fill="x")

tk.Label(card, text="Don't have an account yet?", bg=WHITE, fg=GREY).pack(pady=(10, 0))
tk.Button(card, text="Register here", bg=WHITE, fg=ORANGE, relief="flat", command=show_register).pack()

# ------------------ Register Frame ------------------
register_frame = tk.Frame(container, bg=BG)

header_r = tk.Frame(register_frame, bg=ORANGE, height=150)
header_r.pack(fill="x")
tk.Label(header_r, text="Register", bg=ORANGE, fg=WHITE, font=("Segoe UI", 20, "bold")).pack(pady=50)

card_r = tk.Frame(register_frame, bg=WHITE, bd=0)
card_r.pack(pady=20, padx=20, fill="x")

reg_name, reg_name_error = create_entry(card_r, "Name")
reg_email, reg_email_error = create_entry(card_r, "Email")
reg_phone, reg_phone_error = create_entry(card_r, "Phone Number")
reg_password, reg_password_error = create_entry(card_r, "Password", show="*")
reg_confirm, reg_confirm_error = create_entry(card_r, "Confirm Password", show="*")

def validate_register():
    valid = True
    name = reg_name.get().strip()
    email = reg_email.get().strip()
    phone = reg_phone.get().strip()
    password = reg_password.get()
    confirm = reg_confirm.get()

    # Reset errors
    reg_name_error.config(text="")
    reg_email_error.config(text="")
    reg_phone_error.config(text="")
    reg_password_error.config(text="")
    reg_confirm_error.config(text="")

    if name == "Name" or not name:
        reg_name_error.config(text="Name is required.")
        valid = False
    if email == "Email" or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        reg_email_error.config(text="Invalid email address.")
        valid = False
    if phone == "Phone Number" or not re.match(r"^[0-9]{10}$", phone):
        reg_phone_error.config(text="Enter a valid 10-digit phone number.")
        valid = False
    if password == "Password" or len(password) < 6:
        reg_password_error.config(text="Password must be at least 6 characters.")
        valid = False
    if confirm == "Confirm Password" or password != confirm:
        reg_confirm_error.config(text="Passwords do not match.")
        valid = False

    if valid:
        print("Registration successful (mock)")

tk.Button(card_r, text="Register", bg=ORANGE, fg=WHITE, font=("Segoe UI", 10, "bold"),
          relief="flat", height=2, command=validate_register).pack(pady=15, padx=30, fill="x")

tk.Label(card_r, text="Already have an account?", bg=WHITE, fg=GREY).pack(pady=(10, 0))
tk.Button(card_r, text="Login", bg=WHITE, fg=ORANGE, relief="flat", command=show_login).pack()

# Start with login
show_login()
root.mainloop()
