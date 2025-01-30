import operations
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")
entry = tk.Entry(root, width = 20, font = ("Arial",19), borderwidth=3, relief="solid")
entry.grid(row = 0, column = 0, columnspan=4, pady=20)

def get_input(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))
    
def clear():
    entry.delete(0,tk.END)
    
def evaluate_ops(operation):
    try:
        a = float(get_input())
        if operation == "sqrt":
            result = operations.squareroot(a)
        elif operation == 'log':
            result = operations.logarithm(a)
        elif operation == 'exp':
            result = operations.exp(a)
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
                    result = operations.power(a,b)
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
              command=lambda op=operation: evaluate_ops(op)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=10, height=3, command=clear).grid(row=row, column=0)
        

root.mainloop()