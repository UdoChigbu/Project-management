import tkinter as tk
from tkinter import messagebox, ttk
from storage import save_requirements  # Import function to save requirements to storage

# Function to open the Requirements Tracking form window
def open_window():
    window = tk.Toplevel()  # Create a new top-level window
    window.title("Requirements Tracking")  # Set window title
    window.geometry("600x500")  # Set window size
    window.configure(bg="#1e1e1e")  # Set background to match dark theme

    # Style configuration for buttons
    style = ttk.Style()
    style.theme_use("clam")  # Use 'clam' theme for modern look
    style.configure("DarkBold.TButton", font=("Segoe UI", 10, "bold"), padding=8,
                    background="#6e8f00", foreground="white", relief="flat", borderwidth=0)
    style.map("DarkBold.TButton", background=[("active", "#8aa826"), ("pressed", "#5f7500")])

    # Main frame inside the window
    frame = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Header label
    tk.Label(frame, text="Enter Project Requirements", font=("Segoe UI", 14, "bold"),
             bg="#1e1e1e", fg="white").pack(pady=(0, 10))

    # Functional requirements input
    tk.Label(frame, text="Functional Requirements:", bg="#1e1e1e", fg="white").pack(anchor="w")
    text_functional = tk.Text(frame, height=6, width=60, bg="#2b2b2b", fg="white", insertbackground="white")
    text_functional.pack(pady=(0, 10))

    # Non-functional requirements input
    tk.Label(frame, text="Non-Functional Requirements:", bg="#1e1e1e", fg="white").pack(anchor="w")
    text_non_functional = tk.Text(frame, height=6, width=60, bg="#2b2b2b", fg="white", insertbackground="white")
    text_non_functional.pack(pady=(0, 10))

    # Function to handle form submission
    def submit_requirements():
        functional = text_functional.get("1.0", tk.END).strip().split("\n")
        non_functional = text_non_functional.get("1.0", tk.END).strip().split("\n")
        # Validate that at least one requirement is entered
        if not any(functional) and not any(non_functional):
            messagebox.showerror("Input Error", "Please enter at least one requirement.")
            return
        # Save the data using the storage module
        save_requirements(functional, non_functional)
        messagebox.showinfo("Success", "Requirements saved successfully!")
        window.destroy()

    # Function to cancel/close the form with confirmation
    def cancel():
        if messagebox.askokcancel("Cancel", "Close without saving?"):
            window.destroy()

    # Submit and Cancel buttons
    button_frame = tk.Frame(frame, bg="#1e1e1e")
    button_frame.pack(pady=10)
    ttk.Button(button_frame, text="Submit", command=submit_requirements, style="DarkBold.TButton").pack(side="left", padx=10)
    ttk.Button(button_frame, text="Cancel", command=cancel, style="DarkBold.TButton").pack(side="right", padx=10)
