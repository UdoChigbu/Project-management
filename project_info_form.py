import tkinter as tk
from tkinter import messagebox, ttk
from storage import save_project_info  # Import function to save project info

# Function to open the Project Info form window
def open_window():
    window = tk.Toplevel()  # Create a new top-level window
    window.title("Project Info Form")  # Set window title
    window.geometry("600x600")  # Set window size
    window.configure(bg="#1e1e1e")  # Set dark theme background color

    # Define custom button styling (olive lime green, bold white text)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("DarkBold.TButton", font=("Segoe UI", 10, "bold"), padding=8,
                    background="#6e8f00", foreground="white", relief="flat", borderwidth=0)
    style.map("DarkBold.TButton", background=[("active", "#8aa826"), ("pressed", "#5f7500")])

    # Create the main form container with padding
    frame = tk.Frame(window, bg="#1e1e1e", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Project Manager input
    tk.Label(frame, text="Project Manager", bg="#1e1e1e", fg="white").pack(anchor="w")
    entry_manager = tk.Entry(frame, width=60, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_manager.pack(pady=5, anchor="w")

    # Team Members input (comma-separated list)
    tk.Label(frame, text="Team Members (comma separated)", bg="#1e1e1e", fg="white").pack(anchor="w")
    entry_team = tk.Entry(frame, width=60, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_team.pack(pady=5, anchor="w")

    # Project Description input
    tk.Label(frame, text="Project Description", bg="#1e1e1e", fg="white").pack(anchor="w")
    entry_description = tk.Text(frame, height=4, width=60, bg="#3a3a3a", fg="white", insertbackground="white")
    entry_description.pack(pady=5, anchor="w")

    # Section for listing risks and their statuses
    tk.Label(frame, text="Risks and Statuses", bg="#1e1e1e", fg="white").pack(anchor="w", pady=(10, 0))
    risk_frame = tk.Frame(frame, bg="#1e1e1e")
    risk_frame.pack(anchor="w")

    # Column headers for risk and status
    tk.Label(risk_frame, text="Risk", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w")
    tk.Label(risk_frame, text="Status", bg="#1e1e1e", fg="white").grid(row=0, column=1, sticky="w")

    risk_entries = []  # List to store all risk/status entry pairs

    # Function to add a new row of risk and status entry fields
    def add_risk_row():
        row = len(risk_entries) + 1
        risk_entry = tk.Entry(risk_frame, width=30, bg="#3a3a3a", fg="white", insertbackground="white")
        status_entry = tk.Entry(risk_frame, width=20, bg="#3a3a3a", fg="white", insertbackground="white")
        risk_entry.grid(row=row, column=0, padx=5, pady=2)
        status_entry.grid(row=row, column=1, padx=5, pady=2)
        risk_entries.append((risk_entry, status_entry))

    add_risk_row()  # Add the initial risk row

    # Function to collect and save all entered project info
    def submit_info():
        description = entry_description.get("1.0", tk.END).strip()
        manager = entry_manager.get().strip()
        team = entry_team.get().strip().split(",")
        risks = []

        # Extract all risk and status pairs
        for risk_entry, status_entry in risk_entries:
            risk = risk_entry.get().strip()
            status = status_entry.get().strip()
            if risk and status:
                risks.append((risk, status))

        # Validate required fields
        if not description or not manager or not any(team):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        # Save the data
        save_project_info(description, manager, team, risks)
        messagebox.showinfo("Success", "Project info saved successfully!")
        window.destroy()

    # Function to cancel the form with confirmation
    def cancel():
        if messagebox.askokcancel("Cancel", "Close without saving?"):
            window.destroy()

    # Button to add another risk/status row
    tk.Button(frame, text="+ Add Another Risk", command=add_risk_row,
              bg="#6e8f00", fg="white", relief="flat").pack(pady=10, anchor="w")

    # Submit and Cancel buttons
    button_frame = tk.Frame(frame, bg="#1e1e1e", pady=10)
    button_frame.pack()
    ttk.Button(button_frame, text="Submit", command=submit_info, style="DarkBold.TButton").pack(side="left", padx=10)
    ttk.Button(button_frame, text="Cancel", command=cancel, style="DarkBold.TButton").pack(side="right", padx=10)
