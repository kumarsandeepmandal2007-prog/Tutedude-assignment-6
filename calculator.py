import tkinter as tk
from tkinter import messagebox

# Function to click buttons
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        expression = entry.get()

        if "+" in expression:
            num1, num2 = expression.split("+")
            result = float(num1) + float(num2)

        elif "-" in expression:
            num1, num2 = expression.split("-")
            result = float(num1) - float(num2)

        elif "*" in expression:
            num1, num2 = expression.split("*")
            result = float(num1) * float(num2)

        elif "/" in expression:
            num1, num2 = expression.split("/")
            if float(num2) == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = float(num1) / float(num2)

        else:
            messagebox.showerror("Error", "Invalid Input")
            return

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            button = tk.Button(frame, text=btn, font=("Arial", 18),
                               command=calculate)
        else:
            button = tk.Button(frame, text=btn, font=("Arial", 18),
                               command=lambda b=btn: click(b))
        button.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 18),
                      command=clear, bg="red", fg="white")
clear_btn.pack(fill="both")

root.mainloop()
