# Enhanced Mini Expert System: University Logic Rules
# With CSV Logging for Record-Keeping

import csv
import os
from datetime import datetime

# ---------------------------
# Logic Functions
# ---------------------------
def impl(P, Q):
    return (not P) or Q  # Implication (P → Q)

def tf(b: bool) -> str:
    return "T" if b else "F"

def ask_bool(prompt: str) -> bool:
    # Robust T/F input
    while True:
        v = input(prompt).strip().upper()
        if v in ("T", "F"):
            return v == "T"
        print("Please enter T or F.")

# ---------------------------
# Logger
# ---------------------------
CSV_PATH = "logic_results.csv"

def log_result(student_name, rule_name, result):
    # Logs results to CSV (use UTF-8)
    try:
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), student_name, rule_name, result])
    except Exception as e:
        print(f"Failed to write log: {e}")

# ---------------------------
# Rule 1: Attendance
# ---------------------------
def attendance_rule(student_name):
    print("\n--- Attendance Rule Checker ---")
    late = ask_bool("Is the student late? (T/F): ")
    excuse = ask_bool("Did the student bring an excuse letter? (T/F): ")

    result = impl(late, excuse)
    outcome = "Satisfied ✓" if result else "Violated ✗"

    print(f"P = {tf(late)} (Late), Q = {tf(excuse)} (Excuse Letter)")
    print("Result:", outcome)

    log_result(student_name, "Attendance Rule", outcome)

# ---------------------------
# Rule 2: Grading
# ---------------------------
def grading_rule(student_name):
    print("\n--- Grading Rule Checker ---")
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid grade input.")
        return

    P = grade >= 75  # Passing threshold
    Q = grade >= 75  # Student passes if ≥ 75

    result = impl(P, Q)
    outcome = "Satisfied ✓" if result else "Violated ✗"

    print(f"P = {tf(P)} (grade ≥ 75), Q = {tf(Q)} (student passes)")
    print("Result:", outcome)

    log_result(student_name, "Grading Rule", outcome)

# ---------------------------
# Rule 3: Login System
# ---------------------------
def login_rule(student_name):
    print("\n--- Login Rule Checker ---")
    correct_password = "admin123"
    attempt = input("Enter password: ")

    P = (attempt == correct_password)  # Password correct?
    Q = (attempt == correct_password)  # Access granted if correct

    result = impl(P, Q)
    outcome = "Access granted ✓" if result else "Access denied ✗"

    print(f"P = {tf(P)} (Password Correct), Q = {tf(Q)} (Access Granted)")
    print("Result:", outcome)

    log_result(student_name, "Login Rule", outcome)

# ---------------------------
# Rule 4: Bonus Points
# ---------------------------
def bonus_rule(student_name):
    print("\n--- Bonus Points Eligibility Checker ---")
    regular = ask_bool("Does the student have regular attendance? (T/F): ")
    bonus = regular  # Eligible if regular

    result = impl(regular, bonus)
    outcome = "Satisfied ✓" if result else "Violated ✗"

    print(f"P = {tf(regular)} (Regular Attendance), Q = {tf(bonus)} (Bonus Eligible)")
    print("Result:", outcome)

    log_result(student_name, "Bonus Rule", outcome)

# ---------------------------
# New Rule: Library Borrowing
# If ID is valid → Allowed to borrow books
# ---------------------------
def library_rule(student_name):
    print("\n--- Library Borrowing Checker ---")
    id_valid = ask_bool("Is the student's ID valid? (T/F): ")
    allowed = id_valid  # Allowed to borrow if ID valid

    result = impl(id_valid, allowed)
    outcome = "Allowed to borrow ✓" if result else "Not allowed to borrow ✗"

    print(f"P = {tf(id_valid)} (ID Valid), Q = {tf(allowed)} (Allowed to Borrow)")
    print("Result:", outcome)

    log_result(student_name, "Library Borrowing Rule", outcome)

# ---------------------------
# New Rule: Enrollment Clearance
# If fees are paid → Enrollment confirmed
# ---------------------------
def enrollment_rule(student_name):
    print("\n--- Enrollment Clearance Checker ---")
    fees_paid = ask_bool("Are the student's fees paid? (T/F): ")
    enrollment_confirmed = fees_paid

    result = impl(fees_paid, enrollment_confirmed)
    outcome = "Enrollment confirmed ✓" if result else "Enrollment not confirmed ✗"

    print(f"P = {tf(fees_paid)} (Fees Paid), Q = {tf(enrollment_confirmed)} (Enrollment Confirmed)")
    print("Result:", outcome)

    log_result(student_name, "Enrollment Clearance Rule", outcome)

# ---------------------------
# New Rule: Laboratory Access
# If safety gear is worn → Access granted
# ---------------------------
def lab_rule(student_name):
    print("\n--- Laboratory Access Checker ---")
    safety_gear = ask_bool("Is the required safety gear worn? (T/F): ")
    access_granted = safety_gear

    result = impl(safety_gear, access_granted)
    outcome = "Access granted ✓" if result else "Access denied ✗"

    print(f"P = {tf(safety_gear)} (Safety Gear Worn), Q = {tf(access_granted)} (Access Granted)")
    print("Result:", outcome)

    log_result(student_name, "Laboratory Access Rule", outcome)

# ---------------------------
# Main Menu
# ---------------------------
def main():
    print("=== University Logic Rules System ===")
    student_name = input("Enter student name: ").strip()

    while True:
        print("\n===========================")
        print("          Main Menu        ")
        print("===========================")
        print("1) Attendance Rule Checker")
        print("2) Grading Rule Checker")
        print("3) Login System Rule Checker")
        print("4) Bonus Points Checker")
        print("5) Library Borrowing Checker")
        print("6) Enrollment Clearance Checker")
        print("7) Laboratory Access Checker")
        print("8) Exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            attendance_rule(student_name)
        elif choice == "2":
            grading_rule(student_name)
        elif choice == "3":
            login_rule(student_name)
        elif choice == "4":
            bonus_rule(student_name)
        elif choice == "5":
            library_rule(student_name)
        elif choice == "6":
            enrollment_rule(student_name)
        elif choice == "7":
            lab_rule(student_name)
        elif choice == "8":
            print(f"Exiting... Results saved to {CSV_PATH}")
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------------
# Entry Point
# ---------------------------
if __name__ == "__main__":
    # Create CSV with headers if not exists
    if not os.path.exists(CSV_PATH):
        try:
            with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Student Name", "Rule", "Result"])
        except Exception as e:
            print(f"Failed to create log file: {e}")

    main()
