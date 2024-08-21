import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def save_data(name, weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_data
                 (date TEXT, name TEXT, weight REAL, height REAL, bmi REAL, category TEXT)''')
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO bmi_data VALUES (?, ?, ?, ?, ?, ?)", (date, name, weight, height, bmi, category))
    conn.commit()
    conn.close()

def on_calculate():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        save_data(name, weight, height, bmi, category)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_view_data():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT date, bmi FROM bmi_data WHERE name = ?", (name_entry.get(),))
    data = c.fetchall()
    conn.close()
    if data:
        dates, bmis = zip(*data)
        plt.plot(dates, bmis, marker='o')
        plt.xlabel('Date')
        plt.ylabel('BMI')
        plt.title('BMI Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("Info", "No data available for the specified user.")

app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Weight (kg):").pack()
weight_entry = tk.Entry(app)
weight_entry.pack()

tk.Label(app, text="Height (m):").pack()
height_entry = tk.Entry(app)
height_entry.pack()

tk.Button(app, text="Calculate BMI", command=on_calculate).pack()

result_label = tk.Label(app, text="")
result_label.pack()

tk.Button(app, text="View Data", command=on_view_data).pack()

app.mainloop()
