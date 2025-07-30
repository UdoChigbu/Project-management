import tkinter as tk
from tkinter import messagebox, ttk
from storage import save_employee_effort  # Import function to save effort log

# Open the Effort Logging window
def open_window():
    window = tk.Toplevel()
    window.title("Effort Logging")
    window.geometry("600x500")
    window.configure(bg="#1e1e1e")  # Set dark background

    # Define button and dropdown styles
    style = ttk.Style()
    style.theme_use("clam")

    # Style for submit/cancel buttons
    style.configure("DarkBold.TButton", font=("Segoe UI", 10, "bold"), padding=8,
                    background="#6e8f00", foreground="white", relief="flat", borderwidth=0)
    style.map("DarkBold.TButton", background=[("active", "#8aa826"), ("pressed", "#5f7500")])

    # Style for combobox (dropdown)
    style.configure("Olive.TCombobox",
                    foreground="white",
                    background="#3a3a3a",
                    fieldbackground="#3a3a3a",
                    arrowcolor="#a3c400",
                    selectbackground="#3a3a3a",
                    selectforeground="white")
    style.map("Olive.TCombobox",
              fieldbackground=[('readonly', '#3a3a3a')],
              background=[('readonly', '#3a3a3a')],
              foreground=[('readonly', 'white')],
              arrowcolor=[('readonly', '#a3c400')])

    # Frame to hold all form content
    frame = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Title label
    tk.Label(frame, text="Effort Logging", font=("Segoe UI", 14, "bold"), bg="#1e1e1e", fg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Name input
    tk.Label(frame, text="Name:", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="e", pady=5)
    entry_name = tk.Entry(frame, width=40, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_name.grid(row=1, column=1, pady=5)

    # Category dropdown
    tk.Label(frame, text="Category:", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="e", pady=5)
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(frame, textvariable=category_var, width=38, state="readonly", style="Olive.TCombobox")
    category_dropdown['values'] = ["Requirements", "Design", "Coding", "Testing", "Project Management"]
    category_dropdown.grid(row=2, column=1, pady=5)

    # Requirement input
    tk.Label(frame, text="Requirement:", bg="#1e1e1e", fg="white").grid(row=3, column=0, sticky="e", pady=5)
    entry_requirement = tk.Entry(frame, width=40, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_requirement.grid(row=3, column=1, pady=5)

    # Hours input
    tk.Label(frame, text="Hours:", bg="#1e1e1e", fg="white").grid(row=4, column=0, sticky="e", pady=5)
    entry_hours = tk.Entry(frame, width=40, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_hours.grid(row=4, column=1, pady=5)

    # Comments input
    tk.Label(frame, text="Comments:", bg="#1e1e1e", fg="white").grid(row=5, column=0, sticky="ne", pady=5)
    entry_comments = tk.Text(frame, height=4, width=30, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_comments.grid(row=5, column=1, pady=5)

    # Save entered effort log data
    def submit_effort():
        name = entry_name.get().strip()
        category = category_var.get().strip()
        requirement = entry_requirement.get().strip()
        hours = entry_hours.get().strip()
        comments = entry_comments.get("1.0", tk.END).strip()

        # Validate required fields
        if not name or not category or not requirement or not hours:
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return

        # Check if hours is a valid number
        try:
            hours = float(hours)
        except ValueError:
            messagebox.showerror("Input Error", "Hours must be a number.")
            return

        # Save data to file
        save_employee_effort(name, category, requirement, hours, comments)
        messagebox.showinfo("Success", "Effort logged successfully!")
        window.destroy()

    # Cancel the form with confirmation
    def cancel():
        if messagebox.askokcancel("Cancel", "Close without saving?"):
            window.destroy()

    # Submit and Cancel buttons
    button_frame = tk.Frame(frame, bg="#1e1e1e")
    button_frame.grid(row=6, column=0, columnspan=2, pady=15)

    ttk.Button(button_frame, text="Submit", command=submit_effort, style="DarkBold.TButton").pack(side="left", padx=10)
    ttk.Button(button_frame, text="Cancel", command=cancel, style="DarkBold.TButton").pack(side="right", padx=10)
