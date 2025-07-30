import tkinter as tk
from tkinter import ttk
from ui import requirements_form, effort_log, risk_form, summary, project_info_form
from ui.clear_data import clear_all_data


# Create the main application window
root = tk.Tk()
root.title("Pro Flows - Project Management System")
root.geometry("540x480")  # Set window size
root.configure(bg="#1e1e1e")  # Set background color to dark theme

# Configure style for buttons and labels using ttk (Themed Tkinter)
style = ttk.Style()
style.theme_use("clam")  # Modern theme for widget styling

# Define a custom button style: bold font, olive color, white text
style.configure("DarkBold.TButton",
                font=("Segoe UI", 11, "bold"),
                padding=10,
                relief="flat",
                background="#6e8f00",  # Olive-lime green
                foreground="white",
                borderwidth=0)

# Define color transitions when hovering or pressing buttons
style.map("DarkBold.TButton",
          background=[("active", "#8aa826"), ("pressed", "#5f7500")])

# Label style with white text for dark background
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 11))

# Create the header bar at the top of the window
header = tk.Frame(root, bg="#2c2c2c", height=70)
header.pack(fill="x")

# Add title label to the header
header_label = tk.Label(header, text="Pro Flows", fg="white", bg="#2c2c2c", font=("Segoe UI", 22, "bold"))
header_label.pack(pady=15)

# Content area below the header to hold buttons
content = tk.Frame(root, bg="#1e1e1e", pady=20)
content.pack()

# Functions to open each respective form when buttons are clicked
def open_project_info():
    project_info_form.open_window()

def open_requirements():
    requirements_form.open_window()

def open_effort_log():
    effort_log.open_window()

def open_risks():
    risk_form.open_window()

def open_summary():
    summary.open_window()

# List of buttons with labels and corresponding functions
button_texts = [
    ("Project Info", open_project_info),
    ("Requirements Tracking", open_requirements),
    ("Effort Logging", open_effort_log),
    ("Risk Management", open_risks),
    ("Summary Reports", open_summary)
]

# Create and pack each button into the content area
for text, command in button_texts:
    ttk.Button(content, text=text, command=command, style="DarkBold.TButton").pack(
        pady=10, ipadx=20, fill="x", padx=100)
    
    ttk.Button(root, text="Clear All Data", command=clear_all_data).pack(pady=10)


# Start the application's main event loop
root.mainloop()
