import tkinter as tk
from tkinter import messagebox

# Function to be called when the first button is clicked
def greet():
    messagebox.showinfo("Message", "Hello, World!")

# Function to be called when the second button is clicked
def farewell():
    messagebox.showinfo("Message", "Goodbye!")

# Create main application window
root = tk.Tk()
root.title("Popup Window Example")

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create buttons and assign their functions
button1 = tk.Button(frame, text="Say Hello", command=greet)
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(frame, text="Say Goodbye", command=farewell)
button2.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()
