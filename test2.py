import tkinter as tk
import time

def popup(message):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.overrideredirect(True)  # Remove title bar
    label = tk.Label(root, text=message, font=("Arial", 12), bg="yellow")
    label.pack(expand=True, fill="both")
    # Auto close after 5 seconds
    root.after(1000, root.destroy)
    root.mainloop()

popup("message")
