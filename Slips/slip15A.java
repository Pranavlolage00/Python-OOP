import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birthdate_str = entry.get()
        # Convert input string to a date object
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place the widgets
label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.pack(pady=20)

# Run the application
root.mainloop()
