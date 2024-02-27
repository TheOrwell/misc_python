import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to be called when the first button is clicked
def greet():
    messagebox.showinfo("Message", "Hello, World!")

def openLink():
    try:
        subprocess.Popen("openLinks.bat", shell=True)
    except FileNotFoundError:
        print("Batch file not found!")


# Function to be called when the second button is clicked
def farewell():
    messagebox.showinfo("Message", "Goodbye!")

# Create main application window
root = tk.Tk()
root.title("Popup Window Example")
root.geometry("400x300")  # Set the size of the root window (width x height)

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create buttons and assign their functions in the command= portion.

"""
frame.pack(): This method is used to pack and display the frame widget (or any other widget) within its parent 
container. It defines how the frame should be placed inside the parent widget (in this case, it seems the parent widget 
is the main window). frame.pack() with no arguments simply packs the frame with its default options. You can also pass 
additional parameters to customize its placement, such as side, padx, pady, etc., which determine where and how much 
space it takes up.
"""
button1 = tk.Button(frame, text="M172 - Resources", command=openLink)
button1.pack(side=tk.LEFT, padx=5)


"""
button1.pack(): This method is used to pack and display the button widget within its parent container, which in this
case is the frame. It defines how the button should be placed inside the frame. Like frame.pack(), button1.pack() also 
accepts parameters to customize its placement and appearance, such as side, padx, pady, etc.
"""
button2 = tk.Button(frame, text="Say Goodbye", command=farewell)
frame.pack(side=tk.BOTTOM, padx=5)

# Function to create a custom-sized popup window
def custom_popup():
    popup = tk.Toplevel(root)
    popup.title("Custom Popup")
    popup.geometry("300x200")  # Set the size of the popup window
    label = tk.Label(popup, text="This is a custom-sized popup window.")
    label.pack(padx=10, pady=10)

# Create a button to trigger the custom-sized popup window
custom_button = tk.Button(root, text="Custom Popup", command=custom_popup)
custom_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
