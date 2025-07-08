from multiprocessing import Process, Value
import time
import pyautogui
import tkinter as tk

def popup(message, color):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    label = tk.Label(root, text=message, font=("Arial", 12), bg=color)
    label.pack(expand=True, fill="both")
    root.after(1000, root.destroy)
    root.mainloop()

def network_error_fix(network_error):
    while True:
        try:
            try_again_loc = pyautogui.locateCenterOnScreen("network-error.png", confidence=0.8) 
            popup("Network Error Detected", "red")
            pyautogui.click(689, 652)
            time.sleep(10)
        except:
            network_error.value = False
            popup("No Network Error", "gray")
        time.sleep(1)

def start_match(network_error):
    if network_error.value == False:
        while True:
            try:
                attack_button_loc = pyautogui.locateCenterOnScreen("builder-attack-button.png", confidence=0.8)
                popup("Starting Match", "blue")
                pyautogui.click(attack_button_loc)
                time.sleep(0.5)
                find_now_button_loc = pyautogui.locateCenterOnScreen("find-now-button.png", confidence=0.8)
                pyautogui.click(find_now_button_loc)
            except:
                pass
            time.sleep(5)
    pass

def attack(network_error):
    if network_error.value == False:
        while True:
            try:
                battle_machine_loc = pyautogui.locateCenterOnScreen("battle-machine.png", confidence=0.95)
                pyautogui.click(384, 1022)
                time.sleep(0.1)
                pyautogui.click(183, 586)
                time.sleep(10)
                pyautogui.click(384 + 125, 1022)
                time.sleep(0.1)
                pyautogui.moveTo(183, 586)
                pyautogui.mouseDown()
                time.sleep(3)
                pyautogui.mouseUp()
                slots = [1, 2, 3, 4, 5, 6]  # Exclude slot 1 (already used)
                for slot in slots:
                    x = 384 + 125 * slot
                    pyautogui.click(x, 1022)
                    time.sleep(3)
                pyautogui.click(384, 1022)
            except:
                pass
                time.sleep(5)

if __name__ == "__main__":
    network_error = Value('b', False)
    network_error_fix_process = Process(target=network_error_fix, args=(network_error,))
    start_match_process = Process(target=start_match, args=(network_error,))
    attack_process = Process(target=attack, args=(network_error,))

    network_error_fix_process.start()
    start_match_process.start()
    attack_process.start()
    pass