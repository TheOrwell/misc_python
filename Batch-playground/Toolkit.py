import tkinter as tk
import subprocess


def openLink():
    try:
        subprocess.Popen("openLinks.bat", shell=True)
    except FileNotFoundError:
        print("Batch file not found. Did it get moved or renamed?")


# Function to be called when the second button is clicked
def cleanRecycleBin():
    try:
        subprocess.Popen("cleanRecycleBin.bat")
    except FileNotFoundError:
        print("Batch file not found. Did it get moved or renamed?")


# Create main application window
root = tk.Tk()
root.title("Popup Window Example")
root.geometry("1000x200")  # Set the size of the root window (width x height)

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
button2 = tk.Button(frame, text="Clean Recycle Bin", command=cleanRecycleBin)
button2.pack(side=tk.BOTTOM, padx=5)


# Function to create a custom-sized popup window
def custom_popup():
    popup = tk.Toplevel(root)
    popup.title("Custom Popup")
    popup.geometry("500x400")  # Set the size of the popup window
    label = tk.Label(popup, text="[Add about details here]")
    label.pack(padx=10, pady=10)


# Create a button to trigger the custom-sized popup window
custom_button = tk.Button(root, text="About", command=custom_popup)
custom_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
