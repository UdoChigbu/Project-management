import tkinter as tk
from storage import load_effort_logs, load_risks

def open_window():
    window = tk.Toplevel()
    window.title("Summary Report")
    window.geometry("700x500")
    window.configure(bg="#1e1e1e")

    title = tk.Label(window, text="Summary Report", font=("Segoe UI", 16, "bold"), bg="#1e1e1e", fg="white")
    title.pack(pady=10)

    frame = tk.Frame(window, bg="#1e1e1e", padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    # Effort Summary Section
    effort_logs = load_effort_logs()
    tk.Label(frame, text="Effort Summary", font=("Segoe UI", 13, "bold"), bg="#1e1e1e", fg="white").pack(anchor="w")

    if effort_logs:
        for log in effort_logs:
            text = f"{log['name']} spent {log['hours']} hrs on {log['requirement']} ({log['category']})"
            tk.Label(frame, text=text, bg="#1e1e1e", fg="lightgray").pack(anchor="w")
    else:
        tk.Label(frame, text="No effort logs found.", bg="#1e1e1e", fg="gray").pack(anchor="w")

    # Divider
    tk.Label(frame, text=" ", bg="#1e1e1e").pack()

    # Risk Summary Section
    risks = load_risks()
    tk.Label(frame, text="Risk Summary", font=("Segoe UI", 13, "bold"), bg="#1e1e1e", fg="white").pack(anchor="w")

    if risks:
        for risk in risks:
            text = f"Risk: {risk['risk']} | Status: {risk['status']}"
            tk.Label(frame, text=text, bg="#1e1e1e", fg="lightgray").pack(anchor="w")
    else:
        tk.Label(frame, text="No risks found.", bg="#1e1e1e", fg="gray").pack(anchor="w")
