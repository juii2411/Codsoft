import tkinter as tk

# Function to handle button clicks
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

# Clear the entry field
def clear():
    entry.delete(0, tk.END)

# Evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Big Calculator")

# Make window non-resizable (optional)
root.resizable(False, False)

# Entry widget (larger size)
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# List of buttons (text, row, column)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

# Create and place buttons (larger size)
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18),
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=10, pady=10)

# Clear button (larger size)
clear_btn = tk.Button(root, text="C", width=28, height=2, font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Run the GUI
root.mainloop()