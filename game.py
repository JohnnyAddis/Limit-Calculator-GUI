import tkinter as tk
from tkinter import messagebox
import numpy as np

def f(function, x):
    try:
        return eval(function)
    except:
        raise ValueError("Invalid function input")

def calculate_limit():
    try:
        # Get user input
        function_input = function_entry.get()
        variable_input = variable_entry.get()
        point_input = point_entry.get()

        # Replace the variable in the function with 'x'
        function = function_input.replace(variable_input, 'x')
        
        
        if point_input.lower() == 'inf':
            point = np.inf
        elif point_input.lower() == '-inf':
            point = -np.inf
        else:
            point = float(point_input)
        
        # Small delta for numerical approximation
        delta = 1e-5
        
        # Numerical limit calculation
        if point == np.inf:
            result = np.mean([f(function, 1e10 + i * delta) for i in range(-5, 5)])
        elif point == -np.inf:
            result = np.mean([f(function, -1e10 + i * delta) for i in range(-5, 5)])
        else:
            result = np.mean([f(function, point + i * delta) for i in range(-5, 5)])
        
        # Display the result
        result_label.config(text=f"Limit: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Limit Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Function:").grid(row=0, column=0, padx=10, pady=10)
function_entry = tk.Entry(root)
function_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Variable:").grid(row=1, column=0, padx=10, pady=10)
variable_entry = tk.Entry(root)
variable_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Point:").grid(row=2, column=0, padx=10, pady=10)
point_entry = tk.Entry(root)
point_entry.grid(row=2, column=1, padx=10, pady=10)


calculate_button = tk.Button(root, text="Calculate", command=calculate_limit)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Limit: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
