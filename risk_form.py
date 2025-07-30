import tkinter as tk
from tkinter import messagebox, ttk
from storage import save_risk
import os
import json

RISK_FILE = os.path.join("data", "risks.json")

def save_risk(risk, status):
    risks = []
    if os.path.exists(RISK_FILE):
        with open(RISK_FILE, "r") as f:
            try:
                risks = json.load(f)
            except json.JSONDecodeError:
                risks = []

    risks.append({"risk": risk, "status": status})

    with open(RISK_FILE, "w") as f:
        json.dump(risks, f, indent=4)

# Function to open the Risk Management input form window
def open_window():
    window = tk.Toplevel()  # Create a new top-level window
    window.title("Risk Management Form")  # Set window title
    window.geometry("600x500")  # Set size of the window
    window.configure(bg="#1e1e1e")  # Apply dark background

    # Define button styling for olive-colored, bold buttons
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("DarkBold.TButton", font=("Segoe UI", 10, "bold"), padding=8,
                    background="#6e8f00", foreground="white", relief="flat", borderwidth=0)
    style.map("DarkBold.TButton", background=[("active", "#8aa826"), ("pressed", "#5f7500")])

    # Create the main form frame with dark theme styling
    frame = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Title label for the form
    tk.Label(frame, text="Enter Risks and Statuses", font=("Segoe UI", 14, "bold"),
             bg="#1e1e1e", fg="white").pack(pady=5)

    # Container for input fields
    risk_frame = tk.Frame(frame, bg="#1e1e1e")
    risk_frame.pack()

    # Header labels for input columns
    tk.Label(risk_frame, text="Risk", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w")
    tk.Label(risk_frame, text="Status", bg="#1e1e1e", fg="white").grid(row=0, column=1, sticky="w")

    # Entry fields for risk and status, styled to match dark theme
    risk_entry = tk.Entry(risk_frame, width=30, bg="#3a3a3a", fg="white", insertbackground="white")
    status_entry = tk.Entry(risk_frame, width=20, bg="#3a3a3a", fg="white", insertbackground="white")
    risk_entry.grid(row=1, column=0, padx=5, pady=2)
    status_entry.grid(row=1, column=1, padx=5, pady=2)

    # Handles form submission and validation
    def submit_risks():
        risk = risk_entry.get().strip()
        status = status_entry.get().strip()
        if not risk or not status:
            messagebox.showerror("Input Error", "Please enter both risk and status.")
            return
        save_risk(risk, status)
        messagebox.showinfo("Success", f"Risk '{risk}' with status '{status}' recorded.")
        window.destroy()

    # Cancel the form with confirmation
    def cancel():
        if messagebox.askokcancel("Cancel", "Discard entered risks?"):
            window.destroy()

    # Footer frame to hold Submit and Cancel buttons
    btn_frame = tk.Frame(frame, bg="#1e1e1e")
    btn_frame.pack(pady=10)

    # Styled buttons for form actions
    ttk.Button(btn_frame, text="Submit", command=submit_risks, style="DarkBold.TButton").pack(side="left", padx=10)
    ttk.Button(btn_frame, text="Cancel", command=cancel, style="DarkBold.TButton").pack(side="right", padx=10)
