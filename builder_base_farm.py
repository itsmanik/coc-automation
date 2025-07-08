from multiprocessing import Process, Value
import time
import pyautogui
import tkinter as tk

def popup(message):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.overrideredirect(True)  # Remove title bar
    label = tk.Label(root, text=message, font=("Arial", 12), bg="yellow")
    label.pack(expand=True, fill="both")
    # Auto close after 5 seconds
    root.after(500, root.destroy)
    root.mainloop()

def network_error_fix(network_error):
    while True:
        try:
            try_again_loc = pyautogui.locateCenterOnScreen("network-error.png", confidence=0.8) 
            if try_again_loc:
                popup("Network Error Detected")
                pyautogui.click(689, 652)
                time.sleep(10)
        except:
            network_error.Value = False
            popup("No Network Error")
        time.sleep(1)

if __name__ == "__main__":
    network_error = Value('b', False)
    network_error_fix_process = Process(target=network_error_fix, args=(network_error,))
    network_error_fix_process.start()
    pass