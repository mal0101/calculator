import tkinter as tk
import math
from tkinter import messagebox

class Operations:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def remainder(self, a, b):
        return a % b

operations = Operations()

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")

entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, pady=20)

def get_input(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def evaluate(operation):
    try:
        a = float(entry.get())
        entry.delete(0, tk.END)
        
        if operation == 'sqrt':
            result = math.sqrt(a)
        elif operation == 'log':
            result = math.log(a)
        elif operation == 'exp':
            result = math.exp(a)
        else:
            second_window = tk.Toplevel(root)
            second_window.title("Input Second Number")
            second_window.geometry("300x100")
            
            def second_input():
                b = float(second_entry.get())
                second_window.destroy()
                if operation == 'add':
                    result = operations.addition(a, b)
                elif operation == 'subtract':
                    result = operations.subtraction(a, b)
                elif operation == 'multiply':
                    result = operations.multiplication(a, b)
                elif operation == 'divide':
                    result = operations.division(a, b)
                elif operation == 'power':
                    result = math.pow(a, b)
                elif operation == 'remainder':
                    result = operations.remainder(a, b)
                entry.insert(0, result)
                
            second_entry = tk.Entry(second_window, width=10)
            second_entry.pack(pady=10)
            tk.Button(second_window, text="Submit", command=second_input).pack()
            return
        
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

buttons = [
    ('+', 'add'), ('-', 'subtract'), ('*', 'multiply'), ('/', 'divide'),
    ('√', 'sqrt'), ('^', 'power'), ('%', 'remainder'), ('log', 'log'), ('exp', 'exp')
]

row = 1
col = 0

for text, operation in buttons:
    tk.Button(root, text=text, width=10, height=3, 
              command=lambda op=operation: evaluate(op)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=10, height=3, command=clear).grid(row=row, column=0)

root.mainloop()
 