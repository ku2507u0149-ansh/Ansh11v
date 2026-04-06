# ============================================================
#  app.py - Flask Backend for Event Registration System
#  Course: Google Cloud Digital Leader | Capstone Project
# ============================================================

# --- Import required libraries ---
from flask import Flask, render_template, request   # Flask core tools
import csv        # To read/write CSV files
import os         # To check if a file already exists

# --- Create the Flask app ---
app = Flask(__name__)

# --- Constants ---
CSV_FILE = "registrations.csv"
COMMENTS_FILE = "comments.csv"
CSV_HEADERS = [
    "First Name",
    "Last Name",
    "Email",
    "Roll Number",
    "Year",
    "Phone",
    "Notes",
    "Event Name"
]


# ============================================================
#  FUNCTION: Initialize the CSV file
#  Creates the file with headers if it doesn't already exist
# ============================================================
def initialize_csv():
    # If file doesn't exist OR is empty → write header
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADERS)
def initialize_comments_csv():
    if not os.path.exists(COMMENTS_FILE) or os.path.getsize(COMMENTS_FILE) == 0:
        with open(COMMENTS_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Comment"])

# ============================================================
#  FUNCTION: Save registration data to CSV
#  Appends a new row without deleting existing data
# ============================================================
def save_to_csv(first_name, last_name, email, roll_number, year, phone, notes, event_name):
    # ALWAYS ensure header exists
    initialize_csv()

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            first_name,
            last_name,
            email,
            roll_number,
            year,
            phone,
            notes,
            event_name
        ])

def save_comment(name, email, comment):
    initialize_comments_csv()

    with open(COMMENTS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, comment])

# ============================================================
#  FUNCTION: Validate form input
#  Returns an error message string, or None if all is good
# ============================================================
def validate_input(full_name, event_name):
    if not full_name or full_name.strip() == "":
        return "Full Name cannot be empty."
    if not event_name or event_name.strip() == "":
        return "Please select an Event."
    return None   # No error


# ============================================================
#  ROUTE: Home Page  (GET + POST)
#  GET  → Show the registration form
#  POST → Process the submitted form data
# ============================================================
# ============================
# HOME ROUTE (REGISTRATION)
# ============================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()
        email = request.form.get("email", "").strip()
        roll_number = request.form.get("roll_number", "").strip()
        year = request.form.get("year", "").strip()
        phone = request.form.get("phone", "").strip()
        notes = request.form.get("notes", "").strip()
        event_name = request.form.get("event_name", "").strip()

        if not first_name or not last_name or not email or not roll_number or not year or not phone or not event_name:
            return "Error"

        save_to_csv(
            first_name,
            last_name,
            email,
            roll_number,
            year,
            phone,
            notes,
            event_name
        )

        return "OK"

    # 🔥 LOAD COMMENTS TO DISPLAY
    comments = []
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for row in reader:
                comments.append({
                    "name": row[0],
                    "email": row[1],
                    "text": row[2]
                })

    return render_template("index.html", comments=comments)


# ============================
# COMMENT ROUTE
# ============================
from flask import redirect

@app.route("/comment", methods=["POST"])
def comment():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    comment_text = request.form.get("comment", "").strip()

    if not name or not email or not comment_text:
        return redirect("/")   # simple redirect

    save_comment(name, email, comment_text)

    return redirect("/")   # 🔥 BEST PRACTICE

# ============================================================
#  START THE APP
#  debug=True → shows helpful error messages during development
# ============================================================
if __name__ == "__main__":
    initialize_csv()        # Make sure CSV file exists before starting
    app.run(debug=True)     # Start the Flask development server