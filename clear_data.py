import os
import json
from tkinter import messagebox

DATA_FILES = [
    os.path.join("data", "effort_log.json"),
    os.path.join("data", "project_info.json"),
    os.path.join("data", "requirements.json"),
    os.path.join("data", "risks.json"),
]

def clear_all_data():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all saved project data?")
    if not confirm:
        return

    for filepath in DATA_FILES:
        with open(filepath, "w") as f:
            json.dump([], f)  # Or json.dump({}, f) for project_info.json
    messagebox.showinfo("Success", "All data has been cleared.")
