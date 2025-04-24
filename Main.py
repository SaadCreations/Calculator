import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x280")  # Increased height to accommodate branding
root.resizable(False, False)

# Create input fields
tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Create operation selection
tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=10)
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])  # Default value
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Add branding label
branding_label = tk.Label(root, text="SAAD CREATIONS", font=("Arial", 8, "bold"), fg="#666666")
branding_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
