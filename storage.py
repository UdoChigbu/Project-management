import os
import json

# Define the path to the data directory (relative to this file)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# Create the data directory if it doesn't already exist
os.makedirs(DATA_DIR, exist_ok=True)

# Define paths to the specific data files
PROJECT_INFO_FILE = os.path.join(DATA_DIR, "project_info.json")
REQUIREMENTS_FILE = os.path.join(DATA_DIR, "requirements.json")
EFFORT_LOG_FILE = os.path.join(DATA_DIR, "effort_log.json")

# Save project information (manager, team, risks) to a JSON file
def save_project_info(description, manager_name, team_members, risks):
    data = {
        "description": description,
        "manager": manager_name,
        "team_members": team_members,
        "risks": [{"risk": r, "status": s} for r, s in risks]  # Convert tuple list to dict format
    }
    # Write the data to project_info.json with indentation
    with open(PROJECT_INFO_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Save functional and non-functional requirements to a JSON file
def save_requirements(functional_reqs, non_functional_reqs):
    data = {
        "functional": functional_reqs,
        "non_functional": non_functional_reqs
    }
    # Write the data to requirements.json with indentation
    with open(REQUIREMENTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Save an employee's effort log to a JSON file
def save_employee_effort(name, category, requirement, effort_hours, comments=""):
    log_entry = {
        "name": name,
        "category": category,
        "requirement": requirement,
        "hours": effort_hours,
        "comments": comments
    }

    # Load existing effort logs if the file exists
    if os.path.exists(EFFORT_LOG_FILE):
        with open(EFFORT_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []  # Start fresh if file is empty or corrupt
    else:
        logs = []  # Start with an empty log if file doesn't exist

    # Append the new entry to the log list
    logs.append(log_entry)

    # Write the updated log back to the file
    with open(EFFORT_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

EFFORT_LOG_FILE = os.path.join("data", "effort_log.json")
RISK_FILE = os.path.join("data", "risks.json")

def load_effort_logs():
    if os.path.exists(EFFORT_LOG_FILE):
        with open(EFFORT_LOG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def load_risks():
    if os.path.exists(RISK_FILE):
        with open(RISK_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []        

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